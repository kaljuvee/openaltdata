import logging
import feedparser
import data_collection.altdata_service.news.config.sqlalchemy_connector as dbconn
import data_collection.altdata_service.news.util.news_util as news_util
import model.news.sentiment_util as sentiment_util

news = dbconn.db.Table('news', dbconn.metadata, autoload=True, autoload_with=dbconn.engine)

SENTI_METHOD = 'txtblob_vader'
default_language = 'en'
logging.basicConfig(level=logging.INFO)
COMPANY_KEY = 'COMPANY_KEY'
MARKET_KEY = 'MARKET_KEY'

def process_news(market_news_urls, company_news_url):
    for key, url in market_news_urls.items():
        store_news(key, MARKET_KEY, url)

    for key, url in company_news_url.items():
        store_news(key, COMPANY_KEY, url)

def store_news(key, key_type, rss_url):
    feed = feedparser.parse(rss_url)
    market_news_df = news_util.get_news_df()
    for newsitem in feed['items']:
        if (news_util.check_news_item(newsitem['link']) is not True):
            print('storing news item: ', key, ': ', newsitem['title'])
            try:
                market_news_df = market_news_df.append({'title': newsitem['title'],
                                  'summary': news_util.clean_text(newsitem['summary']),
                                  'published': newsitem['published'],
                                  'link': newsitem['link'],
                                  'keyword': news_util.get_keyword(newsitem),
                                  'contributor': news_util.get_contributor(newsitem),
                                  'language': news_util.get_language(newsitem),
                                  'ticker': news_util.get_ticker(newsitem),
                                  'ticker_source': news_util.get_ticker_source(newsitem),
                                  'trading_session': news_util.get_trading_session(newsitem),
                                  'yticker': news_util.get_yticker(newsitem, key, key_type),
                                  'ticker_normal': news_util.get_yticker(newsitem, key, key_type),
                                  'senti_method': sentiment_util.BLENDED_METHOD,
                                  'provider': newsitem['publisher']}, ignore_index=True)

                market_news_df['senti_score'] = market_news_df['summary'].apply(lambda x: sentiment_util.get_textblob_sentiment(x))
                market_news_df['senti_score'] =  market_news_df['senti_score'].astype(float)
                market_news_df['published'] = market_news_df['published'].astype('datetime64[ns]')
                market_news_df.to_sql(news, dbconn.conn, if_exists='append', index=False)
            except Exception as e:
                print('Exception in store_news:', e)
            pass

def main():
    market_rss_urls = news_util.load_market_rss_urls()
    company_rss_urls = news_util.load_company_rss_urls()
    process_news(market_rss_urls, company_rss_urls)

if __name__ == "__main__":
    main()