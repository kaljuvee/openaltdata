from bs4 import BeautifulSoup
import data_collection.altdata_service.news.util.ticker_extractor as tx
import model.news.sentiment_util as sentiment_util
from langdetect import detect
from datetime import datetime
from pandas import to_datetime

DEFAULT_SESSION = 'pre-market'
COMPANY_KEY = 'COMPANY_KEY'


class NewsItemProcessor:
    """Extracts all useful information about a news article into dictionary"""

    def __init__(self, news_item, key, key_type):
        self.news_item = news_item
        self.key = key
        self.key_type = key_type
        self.found_with_trit_api = False
        self.news_data_dict_list = []

    def process_item(self):

        unprocessed_ticker = self.news_item['category'] if 'category' in self.news_item else None
        extractor = tx.TickerExtractor(
            summary=self.__get_summary(),
            link=self.__get_link(),
            unprocessed_ticker=unprocessed_ticker
        )
        extractor.process_arguments()

        self.found_with_trit_api = extractor.found_ticker_with_trit_api

        for ticker_index in range(len(extractor.unprocessed_ticker_list)):

            self.news_data_dict_list.append({
                'title': self.__get_title(),
                'summary': self.__get_summary(),
                'published': self.__get_published(),
                'link': self.__get_link(),
                'keyword': self.__get_keyword(),
                'contributor': self.__get_contributor(),
                'company': self.__get_company(),
                'language': self.__get_language(),
                'ticker': extractor.unprocessed_ticker_list[ticker_index],
                'ticker_source': self.__get_ticker_source(extractor.ticker_list[ticker_index]),
                'yticker': self.__get_yticker(extractor.ticker_list[ticker_index]),
                'ticker_normal': extractor.ticker_normal_list[ticker_index],
                'exchange': extractor.exchange_list[ticker_index],
                'trading_session': self.__get_trading_session(),
                'senti_method': self.__get_senti_method(),
                'senti_score': self.__get_senti_score(),
                'provider': self.__get_provider()})

        return self.news_data_dict_list

    @staticmethod
    def extract_text_from_html(raw_html):
        return BeautifulSoup(raw_html, "lxml").text

    def __get_title(self):
        return self.news_item['title'] if 'title' in self.news_item else None

    def __get_summary(self):
        return self.extract_text_from_html(self.news_item['summary']) if 'summary' in self.news_item else None

    def __get_published(self):
        if 'published' in self.news_item:
            datetime_string = str(self.news_item['published']).strip()
            if datetime_string[-2:] == 'UT':
                datetime_string = datetime_string.replace('UT', 'UTC')
            return to_datetime(datetime_string.strip())
        else:
            return None

    def __get_link(self):
        return self.news_item['link'] if 'link' in self.news_item else None

    def __get_keyword(self):
        return self.news_item['dc_keyword'] if 'dc_keyword' in self.news_item else None

    def __get_contributor(self):
        return self.news_item['contributors'][0]['name'] if 'contributors' in self.news_item else None

    def __get_company(self):
        return self.news_item['contributors'][0]['name'] if 'contributors' in self.news_item else None

    def __get_language(self):
        return self.news_item['language'] if 'language' in self.news_item else detect(self.__get_summary())

    def __get_ticker_source(self, ticker):
        if self.found_with_trit_api:
            return 'TRIT'
        elif 'publisher' in self.news_item and ticker is not None:
            return self.news_item['publisher']
        else:
            return 'NA'

    def __get_yticker(self, ticker):
        return self.key if ticker is None and self.key_type == COMPANY_KEY else ticker

    def __get_trading_session(self):
        return DEFAULT_SESSION

    def __get_senti_method(self):
        return sentiment_util.BLENDED_METHOD

    def __get_senti_score(self):
        return sentiment_util.get_blended_sentiment(self.__get_summary())

    def __get_provider(self):
        if'publisher' in self.news_item:
            return self.news_item['publisher']

        link = self.__get_link()

        if 'businesswire' in link:
            return 'Businesswire'
        elif 'globenewswire' in link:
            return 'GlobeNewswire Inc.'
        else:
            return None
