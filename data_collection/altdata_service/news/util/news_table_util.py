import data_collection.altdata_service.news.config.sqlalchemy_connector as dbconn
import pandas as pd
from db.dbutil.news.db_queries_news_data import psql_db_news_data_gcp
import data_collection.altdata_service.news.util.ticker_extractor as tx
import model.news.sentiment_util as sentiment_util

news_table = dbconn.db.Table('news', dbconn.metadata, autoload=True, autoload_with=dbconn.engine)


def delete_duplicates():
    news_df = psql_db_news_data_gcp().get_entire_news_table()
    news_df_duplicates = news_df[news_df.duplicated(subset=['title', 'ticker', 'published', 'senti_score'],
                                                    keep='first')]
    news_df_duplicates = news_df_duplicates.sort_values('published', ascending=False)

    # Print statement required for test_news_table_util.py unit test
    # See data_collection/altdata_service/news/tests/test_news_table_util.py
    print('Deleting', len(news_df_duplicates.index), 'duplicate rows...')
    psql_db_news_data_gcp().delete_from_news_table(df=news_df_duplicates)


def copy_content_from_news_item_to_news():
    df = psql_db_news_data_gcp().select_content_that_does_not_exist_in_news()

    data = []

    count = 0
    found_ric_count = 0

    for i in df.index:
        title = df.at[i, 'title']
        summary = df.at[i, 'summary']
        published = df.at[i, 'published']
        link = df.at[i, 'link']
        provider = df.at[i, 'provider']
        language = df.at[i, 'language']
        extractor = tx.TickerExtractor(summary=summary, link=link)
        extractor.process_arguments()

        for index in range(len(extractor.ticker_list)):
            data.append({
                'title': title,
                'summary': summary,
                'published': published,
                'link': link,
                'provider': provider,
                'language': language,
                'ticker': extractor.unprocessed_ticker_list[index],
                'senti_score': sentiment_util.get_blended_sentiment(summary),
                'senti_method': sentiment_util.BLENDED_METHOD,
                'ticker_source': 'TRIT' if extractor.found_ticker_with_trit_api else 'NA',
                'trading_session': 'pre-market',
                'yticker': extractor.ticker_list[index],
                'ticker_normal': extractor.ticker_normal_list[index],
                'exchange': extractor.exchange_list[index]
            })

        count += 1
        if len(extractor.unprocessed_ticker_list) > 1 or extractor.unprocessed_ticker_list[0] is not None:
            found_ric_count += 1

        print(f"Rows copied: {count:4}, rows where ric was found: {found_ric_count}")

        if count >= 2000:
            break

        if count % 50 == 0:
            print("Inserting collected data...")
            df_to_insert = pd.DataFrame(data)
            psql_db_news_data_gcp().insert_into_news_table(df_to_insert)
            delete_duplicates()
            data = []

    df_to_insert = pd.DataFrame(data)
    psql_db_news_data_gcp().insert_into_news_table(df_to_insert)


if __name__ == '__main__':
    delete_duplicates()
