from sqlalchemy.engine import create_engine
from db.db_access import big_query_access
from sqlalchemy import MetaData, Table
from google.cloud import bigquery
import pandas_gbq as pd_gbq
from google.oauth2 import service_account
import pandas as pd


class big_connector_twitter_mig(object):
    def __init__(self):
        self.path, self.bigquery_uri = big_query_access()
        self.client = bigquery.Client.from_service_account_json(self.path)
        self.credentials = service_account.Credentials.from_service_account_file(self.path,)

    def get_tweet_cashtag_data(self):
        # Perform a query.
        QUERY = ('SELECT * FROM `fedoraltdata.altcap_big.tweet_cashtag` LIMIT 1000')
        query_job = self.client.query(QUERY)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish

    def insert_into_tweet(self, df, table_name):
        """
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

        df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_update'] = df['date_update'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_utc'] = df['date_utc'].dt.strftime('%Y-%m-%d %H:%M:%S')

        df = df[['tweet_id', 'conversation_id', 'date', 'timezone', 'tweet', 'hashtags', 'cashtags',
                 'user_id_str', 'username', 'nlikes', 'nreplies', 'nretweets', 'quote_url', 'reply_to',
                 'date_update', 'company_id', 'sentiment_score_vader', 'sentiment_score_textblob', 'date_utc', 'id', 'link']]
        df['date'] = pd.to_datetime(df['date'])
        df['date_utc'] = pd.to_datetime(df['date_utc'])
        df['date_update'] = pd.to_datetime(df['date_update'])
        """
        # Prepares a reference to the dataset
        dataset_ref = self.client.dataset('altcap_big')

        table_ref = dataset_ref.table(table_name)
        table = self.client.get_table(table_ref)  # API call

        errors = self.client.insert_rows_from_dataframe(table, df)  # API request
        #assert errors == []

    def insert_into_tweet_pandas(self, df, table_name):
        """
        df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_update'] = df['date_update'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['date_utc'] = df['date_utc'].dt.strftime('%Y-%m-%d %H:%M:%S')

        df['tweet_id'] = df['tweet_id'].astype(int)
        df['conversation_id'] = df['conversation_id'].astype(int)
        df['company_id'] = df['company_id'].astype(int)
        df['nlikes'] = df['nlikes'].astype(int)
        df['nreplies'] = df['nreplies'].astype(int)
        df['nretweets'] = df['nretweets'].astype(int)

        df['hashtags'] = df['hashtags'].astype(str)
        df['cashtags'] = df['cashtags'].astype(str)
        df['reply_to'] = df['reply_to'].astype(str)
        df['link'] = df['link'].astype(str)
        """

        pd_gbq.to_gbq(df, 'altcap_big.' + table_name, project_id='fedoraltdata', credentials=self.credentials, if_exists='append')

    def insert_into_tweet_cashtag_old(self, df):
        table_id = 'altcap_big.tweet_cashtag'
        # Since string columns use the "object" dtype, pass in a (partial) schema
        # to ensure the correct BigQuery data type.
        job_config = bigquery.LoadJobConfig(schema=[bigquery.SchemaField("my_string", "STRING"),])

        job = self.client.load_table_from_dataframe(df, table_id, job_config=job_config)

        # Wait for the load job to complete.
        job.result()
        # df.to_gbp('altcap_big.tweet_cashtag')


class big_connector_twitter_mig_sqlalchemy(object):
    def __init__(self):
        self.path, self.bigquery_uri = big_query_access()
        self.engine = create_engine('bigquery://fedoraltdata/altcap_big')
        self.metadata = MetaData(bind=self.engine)
        self.table_name = None
        #self.bigquery_uri = f'bigquery://{fedoraltdata}/{bigquery_dataset}'

    @property
    def table(self):
        if self.table_name:
            return Table(self.table_name, self.metadata, autoload=True)
        return None

    def fetch_rows(self, query, table=None):
        """Fetch all rows via query."""
        rows = self.engine.execute(query).fetchall()
        return rows

    def insert_rows(self, rows, table=None, replace=None):
        """Insert rows into table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {table}')
        self.table_name = table
        self.engine.execute(self.table.insert(), rows)
        return self.construct_response(rows, table)

    @staticmethod
    def construct_response(rows, table):
        """Summarize results of an executed query."""
        columns = rows[0].keys()
        column_names = ", ".join(columns)
        num_rows = len(rows)
        return f'Inserted {num_rows} rows into `{table}` with {len(columns)} columns: {column_names}'
