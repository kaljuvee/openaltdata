import psycopg2
from sqlalchemy import create_engine
import pandas as pd

import db.db_access as access


class RedditConnectorDBAPI(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud_altcap_api()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def ticker_freq_trending(self, pipeline='wsb'):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_REDDIT_TICKER = """SELECT data_json FROM reddit_ticker WHERE pipeline='{PIPE}' ORDER BY compute_datetime DESC LIMIT 1"""
        query = CONST_SQL_GET_REDDIT_TICKER.format(PIPE=str(pipeline))
        cur.execute(query)
        result = cur.fetchall()
        return result[0][0]

    def insert_reddit_data_api(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'reddit_ticker'

            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return
