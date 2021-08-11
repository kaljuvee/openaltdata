from sqlalchemy.engine import create_engine
from db.db_access import big_query_access
from sqlalchemy import MetaData, Table
from google.cloud import bigquery
import pandas_gbq as pd_gbq
from google.oauth2 import service_account
import pandas as pd
from datetime import datetime


class Twitter_bigquery_connector_keyword_db(object):
    def __init__(self):
        self.path, self.bigquery_uri = big_query_access()
        self.client = bigquery.Client.from_service_account_json(self.path)
        self.credentials = service_account.Credentials.from_service_account_file(self.path,)

    def get_tweet_data(self):
        # Perform a query.
        query = 'SELECT * FROM `fedoraltdata.altcap_big.tweet` LIMIT 1000'
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_last_date_tweet(self, company_id):
        # Perform a query.
        query = 'SELECT MAX(date) FROM `fedoraltdata.altcap_big.tweet` WHERE company_id = {COMPANY_ID};'
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()
        if df.loc[0][0] is pd.NaT:
            return pd.DataFrame()
        else:
            return df.loc[0][0]

    def get_min_date_tweet(self, company_id):
        # Perform a query.
        query = 'SELECT MIN(date) FROM `fedoraltdata.altcap_big.tweet` WHERE company_id = {COMPANY_ID};'
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()
        return df.loc[0][0]

    def last_id_from_last_tweet(self, company_id, last_date):
        # Perform a query.
        query = """SELECT id FROM `fedoraltdata.altcap_big.tweet` WHERE company_id = {COMPANY_ID} AND date = '{DATE}';"""
        query = query.format(COMPANY_ID=str(company_id), DATE=str(last_date))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()
        return df.loc[0][0]

    def get_all_dates_from_ticker(self, company_id):
        query = """Select DATE(date) AS date from `fedoraltdata.altcap_big.tweet` WHERE company_id = {COMPANY_ID} group by date order by date"""
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_tweets_details(self):
        query = """SELECT MAX(date) as max_date, company_id FROM `fedoraltdata.altcap_big.tweet` group by company_id"""
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish

        for i in df.index:
            df.at[i, 'max_date'] = df.at[i, 'max_date'].to_pydatetime()
        return df

    def get_all_tweets_from_company_id(self, company_id):
        query = """SELECT tweet_id, tweet, id, date_utc FROM `fedoraltdata.altcap_big.tweet` WHERE company_id = {COMPANY_ID}"""
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def create_normal_materialised_view(self):
        query = """DROP table `fedoraltdata.altcap_big.mat_view_normal_tweet`;
                CREATE table `fedoraltdata.altcap_big.mat_view_normal_tweet`
                AS SELECT 
                DISTINCT t.company_id, Date(date) AS date_utc, avg(t.sentiment_score_vader) AS vader, avg(t.sentiment_score_textblob) AS textblob, count(t.id) AS number_tweets
                FROM `fedoraltdata.altcap_big.tweet` t
                WHERE is_spam is False
                GROUP BY t.company_id, date_utc;"""
        query_job = self.client.query(query)  # API request
        query_job.result()  # Waits for query to finish

    def create_10_likes_materialised_view(self):
        query = """DROP table `fedoraltdata.altcap_big.mat_view_more_10_likes_tweet`;
                CREATE table `fedoraltdata.altcap_big.mat_view_more_10_likes_tweet`
                AS SELECT 
                DISTINCT t.company_id, Date(date) AS date_utc, avg(t.sentiment_score_vader) AS vader, avg(t.sentiment_score_textblob) AS textblob, count(t.id) AS number_tweets
                FROM `fedoraltdata.altcap_big.tweet` t
                WHERE (t.nlikes >= 10) AND is_spam is False
                GROUP BY t.company_id, date_utc;"""
        query_job = self.client.query(query)  # API request
        query_job.result()  # Waits for query to finish

    def update_all_rows_false_is_spam(self):
        query = """UPDATE `fedoraltdata.altcap_big.tweet` SET is_spam = False WHERE TRUE;"""
        query_job = self.client.query(query)  # API request
        query_job.result()

    def insert_parsing_tweet(self, df):
        df['tweet_id'] = df['tweet_id'].astype('int64')
        df['conversation_id'] = df['conversation_id'].astype('int64')
        df['date'] = pd.to_datetime(df['date'])
        df['timezone'] = df['timezone'].astype(str)
        df['tweet'] = df['tweet'].astype(str)
        df['hashtags'] = df['hashtags'].astype(str)
        df['cashtags'] = df['cashtags'].astype(str)
        df['user_id_str'] = df['user_id_str'].astype(str)
        df['username'] = df['username'].astype(str)
        df['nlikes'] = df['nlikes'].astype(int)
        df['nreplies'] = df['nreplies'].astype(int)
        df['nretweets'] = df['nretweets'].astype(int)
        df['quote_url'] = df['quote_url'].astype(str)
        df['reply_to'] = df['reply_to'].astype(str)
        df['date_update'] = pd.to_datetime(df['date_update'])
        df['company_id'] = df['company_id'].astype(int)
        df['sentiment_score_vader'] = df['sentiment_score_vader'].astype(float)
        df['sentiment_score_textblob'] = df['sentiment_score_textblob'].astype(float)
        df['date_utc'] = pd.to_datetime(df['date_utc'])
        df['id'] = df['id'].astype('int64')
        df['link'] = df['link'].astype(str)
        """
        df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_update'] = df['date_update'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_utc'] = df['date_utc'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date'] = pd.to_datetime(df['date'])
        df['date_utc'] = pd.to_datetime(df['date_utc'])
        df['date_update'] = pd.to_datetime(df['date_update'])
        """

        pd_gbq.to_gbq(df, 'altcap_big.' + 'tweet', project_id='fedoraltdata', credentials=self.credentials, if_exists='append')
        return

    def check_if_exist_spam_result_tweet(self):
        query = """SELECT COUNT(1) AS cnt FROM `fedoraltdata.altcap_big.__TABLES_SUMMARY__` WHERE table_id = 'spam_result_tweet';"""
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()

        # check if table exists, if 1 then True if no then False
        if df['cnt'].values[0] == 1:
            table_exist = True
        elif df['cnt'].values[0] == 0:
            table_exist = False
        else:
            table_exist = False

        return table_exist

    def insert_spam_result_tweet(self, df):
        pd_gbq.to_gbq(df, 'altcap_big.' + 'spam_result_tweet', project_id='fedoraltdata', credentials=self.credentials, if_exists='append')
        return

    # TODO made some late modifications need to do some tests and check, this pipeline is not being used at the moment
    def label_spam_from_main_table(self):
        query = """UPDATE `fedoraltdata.altcap_big.tweet` AS TableA
                SET TableA.is_spam = True
                WHERE EXISTS (
                SELECT 1
                FROM `fedoraltdata.altcap_big.spam_result_tweet` AS TableB
                WHERE TableA.id = TableB.id
                )"""
        query_job = self.client.query(query)  # API request
        query_job.result()

    def delete_spam_result_tweet_table(self):
        query = """DROP table `fedoraltdata.altcap_big.spam_result_tweet`;"""
        query_job = self.client.query(query)  # API request
        query_job.result()  # Waits for query to finish


class Twitter_bigquery_connector_cashtag_db(object):
    def __init__(self):
        self.path, self.bigquery_uri = big_query_access()
        self.client = bigquery.Client.from_service_account_json(self.path)
        self.credentials = service_account.Credentials.from_service_account_file(self.path,)

    def get_tweet_data(self):
        # Perform a query.
        query = 'SELECT * FROM `fedoraltdata.altcap_big.tweet` LIMIT 1000'
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_last_date_tweet(self, company_id):
        # Perform a query.
        query = 'SELECT MAX(date) FROM `fedoraltdata.altcap_big.tweet_cashtag` WHERE company_id = {COMPANY_ID};'
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()
        if df.loc[0][0] is pd.NaT:
            return pd.DataFrame()
        else:
            return df.loc[0][0]

    def get_min_date_tweet(self, company_id):
        # Perform a query.
        query = 'SELECT MIN(date) FROM `fedoraltdata.altcap_big.tweet_cashtag` WHERE company_id = {COMPANY_ID};'
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()
        return df.loc[0][0]

    def last_id_from_last_tweet(self, company_id, last_date):
        # Perform a query.
        query = """SELECT id FROM `fedoraltdata.altcap_big.tweet_cashtag` WHERE company_id = {COMPANY_ID} AND date = '{DATE}';"""
        query = query.format(COMPANY_ID=str(company_id), DATE=str(last_date))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()
        return df.loc[0][0]

    def get_all_dates_from_ticker(self, company_id):
        query = """Select DATE(date) AS date from `fedoraltdata.altcap_big.tweet_cashtag` WHERE company_id = {COMPANY_ID} group by date order by date"""
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_tweets_details(self):
        query = """SELECT MAX(date) as max_date, company_id FROM `fedoraltdata.altcap_big.tweet_cashtag` group by company_id"""
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish

        for i in df.index:
            df.at[i, 'max_date'] = df.at[i, 'max_date'].to_pydatetime()

        return df

    def get_all_tweets_from_company_id(self, company_id):
        query = """SELECT tweet_id, tweet, id, date_utc FROM `fedoraltdata.altcap_big.tweet_cashtag` WHERE company_id = {COMPANY_ID}"""
        query = query.format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def create_normal_materialised_view(self):
        query = """DROP table `fedoraltdata.altcap_big.mat_view_normal_tweet_cashtag`;
                CREATE table `fedoraltdata.altcap_big.mat_view_normal_tweet_cashtag`
                AS SELECT 
                DISTINCT t.company_id, Date(date) AS date_utc, avg(t.sentiment_score_vader) AS vader, avg(t.sentiment_score_textblob) AS textblob, count(t.id) AS number_tweets
                FROM `fedoraltdata.altcap_big.tweet_cashtag` t
                WHERE is_spam is False AND length(cashtags) - length(replace(cashtags, '$', '')) < 2
                GROUP BY t.company_id, date_utc;"""
        query_job = self.client.query(query)  # API request
        query_job.result()  # Waits for query to finish

    def create_10_likes_materialised_view(self):
        query = """DROP table `fedoraltdata.altcap_big.mat_view_more_10_likes_tweet_cashtag`;
                CREATE table `fedoraltdata.altcap_big.mat_view_more_10_likes_tweet_cashtag`
                AS SELECT 
                DISTINCT t.company_id, Date(date) AS date_utc, avg(t.sentiment_score_vader) AS vader, avg(t.sentiment_score_textblob) AS textblob, count(t.id) AS number_tweets
                FROM `fedoraltdata.altcap_big.tweet_cashtag` t
                WHERE (t.nlikes >= 10) AND is_spam is False AND length(cashtags) - length(replace(cashtags, '$', '')) < 2
                GROUP BY t.company_id, date_utc;"""
        query_job = self.client.query(query)  # API request
        query_job.result()

    def update_all_rows_false_is_spam(self):
        query = """UPDATE `fedoraltdata.altcap_big.tweet_cashtag` SET is_spam = False WHERE TRUE;"""
        query_job = self.client.query(query)  # API request
        query_job.result()

    def label_spam_from_main_table(self):
        query = """UPDATE `fedoraltdata.altcap_big.tweet_cashtag` AS TableA
                SET TableA.is_spam = True
                WHERE EXISTS (
                SELECT 1
                FROM `fedoraltdata.altcap_big.spam_result_tweet_cashtag` AS TableB
                WHERE TableA.id = TableB.id
                )"""
        query_job = self.client.query(query)  # API request
        query_job.result()

    def insert_parsing_tweet(self, df):
        df['tweet_id'] = df['tweet_id'].astype('int64')
        df['conversation_id'] = df['conversation_id'].astype('int64')
        df['date'] = pd.to_datetime(df['date'])
        df['timezone'] = df['timezone'].astype(str)
        df['tweet'] = df['tweet'].astype(str)
        df['hashtags'] = df['hashtags'].astype(str)
        df['cashtags'] = df['cashtags'].astype(str)
        df['user_id_str'] = df['user_id_str'].astype(str)
        df['username'] = df['username'].astype(str)
        df['nlikes'] = df['nlikes'].astype(int)
        df['nreplies'] = df['nreplies'].astype(int)
        df['nretweets'] = df['nretweets'].astype(int)
        df['quote_url'] = df['quote_url'].astype(str)
        df['reply_to'] = df['reply_to'].astype(str)
        df['date_update'] = pd.to_datetime(df['date_update'])
        df['company_id'] = df['company_id'].astype(int)
        df['sentiment_score_vader'] = df['sentiment_score_vader'].astype(float)
        df['sentiment_score_textblob'] = df['sentiment_score_textblob'].astype(float)
        df['date_utc'] = pd.to_datetime(df['date_utc'])
        df['id'] = df['id'].astype('int64')
        df['link'] = df['link'].astype(str)
        """
        df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_update'] = df['date_update'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_utc'] = df['date_utc'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date'] = pd.to_datetime(df['date'])
        df['date_utc'] = pd.to_datetime(df['date_utc'])
        df['date_update'] = pd.to_datetime(df['date_update'])
        """

        pd_gbq.to_gbq(df, 'altcap_big.' + 'tweet_cashtag', project_id='fedoraltdata', credentials=self.credentials, if_exists='append')
        return

    def check_if_exist_spam_result_tweet(self):
        query = """SELECT COUNT(1) AS cnt FROM `fedoraltdata.altcap_big.__TABLES_SUMMARY__` WHERE table_id = 'spam_result_tweet_cashtag';"""
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()

        # check if table exists, if 1 then True if no then False
        if df['cnt'].values[0] == 1:
            table_exist = True
        elif df['cnt'].values[0] == 0:
            table_exist = False
        else:
            table_exist = False

        return table_exist

    def insert_spam_result_tweet(self, df):
        pd_gbq.to_gbq(df, 'altcap_big.' + 'spam_result_tweet_cashtag', project_id='fedoraltdata', credentials=self.credentials, if_exists='append')
        return

    def delete_spam_result_tweet_table(self):
        query = """DROP table `fedoraltdata.altcap_big.spam_result_tweet_cashtag`;"""
        query_job = self.client.query(query)  # API request
        query_job.result()  # Waits for query to finish