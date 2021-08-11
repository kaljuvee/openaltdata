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
        self.credentials = service_account.Credentials.from_service_account_file(self.path, )

    def get_normal_materialised_view(self):
        query = """SELECT * FROM `fedoraltdata.altcap_big.mat_view_normal_tweet`"""
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_sentiment_for_company_id(self, company_id):
        query = """SELECT * FROM `fedoraltdata.altcap_big.mat_view_normal_tweet` WHERE company_id = {COMPANY_ID}""".format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_filtered_sentiment_for_company_id(self, company_id):
        query = """SELECT * FROM `fedoraltdata.altcap_big.mat_view_more_10_likes_tweet` WHERE company_id = {COMPANY_ID}""".format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df


class Twitter_bigquery_connector_cashtag_db(object):
    def __init__(self):
        self.path, self.bigquery_uri = big_query_access()
        self.client = bigquery.Client.from_service_account_json(self.path)
        self.credentials = service_account.Credentials.from_service_account_file(self.path, )

    def get_normal_materialised_view(self):
        query = """SELECT * FROM `fedoraltdata.altcap_big.mat_view_normal_tweet_cashtag`"""
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_sentiment_for_company_id(self, company_id):
        query = """SELECT * FROM `fedoraltdata.altcap_big.mat_view_normal_tweet_cashtag` WHERE company_id = {COMPANY_ID}""".format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df

    def get_filtered_sentiment_for_company_id(self, company_id):
        query = """SELECT * FROM `fedoraltdata.altcap_big.mat_view_more_10_likes_tweet_cashtag` WHERE company_id = {COMPANY_ID}""".format(COMPANY_ID=str(company_id))
        query_job = self.client.query(query)  # API request
        df = query_job.result().to_dataframe()  # Waits for query to finish
        return df
