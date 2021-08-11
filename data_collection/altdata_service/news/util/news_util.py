import os.path
import yaml
import logging
from bs4 import BeautifulSoup
import data_collection.altdata_service.news.config.sqlalchemy_connector as dbconn
from dateutil.parser import parse
import pandas as pd

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
# CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')
# RSS_PATH = os.path.join('config', 'altsignals-market-news-rss.yaml')
MARKET_RSS_PATH = os.path.join(ABS_PATH, '../config', 'altsignals-market-news-rss.yaml')
COMPANY_RSS_PATH = os.path.join(ABS_PATH, '../config', 'altsignals-company-news-rss.yaml')
news = dbconn.db.Table('news', dbconn.metadata, autoload=True, autoload_with=dbconn.engine)
DEFAULT_SESSION = 'pre-market'
GLOBENEWSIRE = 'GlobeNewswire Inc.'
TRIT = 'TRIT'
COMPANY_KEY = 'COMPANY_KEY'


def get_news_df():
    cols = ['title', 'summary', 'full_text', 'published', 'link', 'contributor', 'subject', 'keyword', 'provider',
            'language', 'ticker', 'senti_score', 'senti_method', 'company', 'sector', 'market_cap', 'ticker_source',
            'trading_session', 'yticker', 'ticker_normal']
    return pd.DataFrame(columns=cols)


def get_language(newsitem):
    if 'language' in newsitem:
        language = newsitem['language']
    else:
        return None
    return language


def get_ticker(news_item):
    try:
        if 'category' in news_item:
            if ':' in news_item['category']:
                ticker = news_item['category']
            else:
                ticker = None  # we have no ticker in the article; use TRIT
        else:
            ticker = None
    except Exception as e:
        print('Exception in news_util.get_ticker:', e)
        ticker = None
    return ticker


def get_ticker_source(newsitem):
    if 'publisher' in newsitem:
        return newsitem['publisher']
    else:
        return None


def get_keyword(newsitem):
    if 'dc_keyword' in newsitem:
        return newsitem['dc_keyword']
    else:
        return None


def get_yticker(newsitem, key, key_type):
    ticker = get_ticker(newsitem)
    if ticker is not None and get_ticker_source(newsitem) == GLOBENEWSIRE:
        list_ticker = ticker.split(':')
        return list_ticker[1]
    elif ticker is not None and get_ticker_source(newsitem) == TRIT:
        list_ticker = ticker.split('.')
        return list_ticker[0]
    elif key_type == COMPANY_KEY:
        return key
    else:
        return None


def get_exchange(newsitem, key, key_type):
    ticker = get_ticker(newsitem)
    if ticker is not None and get_ticker_source(newsitem) == GLOBENEWSIRE:
        exchange = ticker.split(':')
        return exchange[0]
    else:
        return None


def get_contributor(newsitem):
    if 'contributors' in newsitem:
        return newsitem['contributors'][0]['name']
    else:
        return None


def get_company(newsitem):
    if 'contributors' in newsitem:
        return newsitem['contributors'][0]['name']
    else:
        return None


def get_trading_session(newsitem):
    utc = parse(newsitem['published'])
    return DEFAULT_SESSION


def clean_text(raw_html):
    cleantext = BeautifulSoup(raw_html, "lxml").text
    return cleantext


def check_news_item(link):
    exists_query = dbconn.connector.select([news.columns.link]).where(news.columns.link == link)
    exists = dbconn.conn.execute(exists_query)
    return exists.scalar() is not None


def load_market_rss_urls():
    with open(MARKET_RSS_PATH) as file:
        news_urls = yaml.full_load(file)
        logging.info(f"Checking {len(news_urls.keys())} market RSS URLs")
        return news_urls


def load_company_rss_urls():
    with open(COMPANY_RSS_PATH) as file:
        news_urls = yaml.full_load(file)
        logging.info(f"Checking {len(news_urls.keys())} company RSS URLs")
        return news_urls
