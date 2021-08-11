import logging
from multiprocessing import Pool

import feedparser
import pandas as pd

import data_collection.altdata_service.news.config.sqlalchemy_connector as dbconn
import data_collection.altdata_service.news.util.news_table_util as news_table_util
import data_collection.altdata_service.news.util.news_util as news_util
import data_collection.altdata_service.news.util.process_news_item as nip
from db.dbutil.news.db_queries_news_data import psql_db_news_data_gcp

news_table = dbconn.db.Table('news', dbconn.metadata, autoload=True, autoload_with=dbconn.engine)

SENTI_METHOD = 'txtblob_vader'
default_language = 'en'
logging.basicConfig(level=logging.INFO)
COMPANY_KEY = 'COMPANY_KEY'
MARKET_KEY = 'MARKET_KEY'
FILTER_OUT_NON_ENGLISH_ARTICLES = True


def store_news(key, key_type, rss_url, df):
    data_df = pd.DataFrame()

    feed = feedparser.parse(rss_url)
    for news_item in feed['items']:
        if not news_item['link'] in df.link:
            article_dict = nip.NewsItemProcessor(news_item, key, key_type).process_item()
            article_df = pd.DataFrame(article_dict)
            data_df = data_df.append(article_df, ignore_index=True)

    if FILTER_OUT_NON_ENGLISH_ARTICLES and len(data_df.index) > 0:
        data_df = data_df.loc[data_df['language'] == 'en']

    logging.info(f"Number of articles found from {key}: {len(data_df.index)}")
    return data_df


def main():
    market_rss_urls = news_util.load_market_rss_urls()
    company_rss_urls = news_util.load_company_rss_urls()

    pool_param_combinations = []

    news_df = psql_db_news_data_gcp().get_entire_news_table()

    for key, url in market_rss_urls.items():
        pool_param_combinations.append((key, MARKET_KEY, url, news_df))

    for key, url in company_rss_urls.items():
        pool_param_combinations.append((key, COMPANY_KEY, url, news_df))

    with Pool() as pool:
        list_of_result_dataframes = pool.starmap(store_news, tuple(pool_param_combinations))

    news_df.drop('news_id', inplace=True, axis=1)
    result_df = pd.concat(list_of_result_dataframes)

    subset = ['title', 'ticker', 'published', 'senti_score']
    result_df.drop_duplicates(subset=subset, keep='first', inplace=True)

    news_df = news_df[result_df.columns.tolist()]
    news_df = news_df.astype(result_df.dtypes.to_dict())

    result_df = pd.concat([news_df, news_df, result_df], ignore_index=True)
    result_df.drop_duplicates(subset=subset, keep=False, inplace=True)

    logging.info(f'Inserting {len(result_df.index)} rows into database')
    psql_db_news_data_gcp().insert_into_news_table(df=result_df)
    news_table_util.delete_duplicates()


if __name__ == "__main__":
    main()
