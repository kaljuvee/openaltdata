import db.db_access as access
from db.dbutil.news.sqlalchemy_connector import get_sqlalchemy_connector

import psycopg2
import pandas as pd


class NewsConnectorDb(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud_news()

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_news_sentiment_best(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = """
            select distinct published as date, title as headline, summary, link, provider, yticker as ticker, company, senti_score as signal
            from news n
            where yticker is not null and company is not null and exchange in ('Nasdaq', 'NYSE', 'AMEX') and senti_score > 0 and published > NOW() - INTERVAL '7 days'
            order by senti_score desc limit 15
            """
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        finally:
            cur.close()

    def get_news_sentiment_worst(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = """
            select distinct published as date, title as headline, summary, link, provider, yticker as ticker, company, senti_score as signal
            from news n
            where yticker is not null and company is not null and exchange in ('Nasdaq', 'NYSE', 'AMEX') and senti_score < 0 and published > NOW() - INTERVAL '7 days'
            order by senti_score limit 15
            """
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        finally:
            cur.close()

    def get_news_sentiment_map(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = """
            select distinct published as date, title as headline, summary, link, provider, yticker as ticker, company, senti_score as signal, sector, market_cap
            from news n
            where yticker is not null and company is not null and exchange in ('Nasdaq', 'NYSE', 'AMEX')
            order by published desc limit 100
            """
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        finally:
            cur.close()