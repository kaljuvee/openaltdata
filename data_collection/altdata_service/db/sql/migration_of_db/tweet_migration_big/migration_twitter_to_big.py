from db.sql.migration_of_db.tweet_migration_big.psql_tweet_mig_queries import psql_connector_twitter_mig
from db.sql.migration_of_db.tweet_migration_big.big_queries_sql import big_connector_twitter_mig
import data_collection.altdata_service.twitter.object_function.tweet_cleaner as cleaner


def migration_tweet_tables():
    print('start tweet migration')
    #tweet_mig(table_name='tweet_clone')
    print('start tweet_castag migration')
    tweet_mig(table_name='tweet_cashtag_clone')
    print('job done')


def tweet_mig(table_name):
    psql_conn = psql_connector_twitter_mig()
    big_conn = big_connector_twitter_mig()

    tweet_df = psql_conn.get_twitter(table_name)

    t = 0

    while not tweet_df.empty:

        bi_table = table_name.replace('_clone', '')

        tweet_df = psql_conn.get_twitter(table_name)

        if tweet_df.empty:
            break

        tweet_df = cleaner.clean_df_for_db(tweet_df)

        big_conn.insert_into_tweet(df=tweet_df, table_name=bi_table)

        psql_conn.delete_imported_tweets(df=tweet_df, table_name=table_name)

        t += len(tweet_df)

        print('we have processed ' + str(t) + ' rows')


if __name__ == "__main__":
    migration_tweet_tables()
