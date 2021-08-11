import psycopg2
import pandas as pd

from sqlalchemy import create_engine
import db.db_access as access


class PSQLInternalData(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_main_company(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_MAIN_COMPANY = 'SELECT * FROM maincompany'
            cur.execute(CONST_SQL_GET_MAIN_COMPANY)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_main_company_detail_from_ticker_bbg(self, ticker_bbg):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_MAIN_COMPANY = """SELECT * FROM maincompany WHERE ticker_bbg = '{TICKER}' LIMIT 1""".format(TICKER=str(ticker_bbg))
            cur.execute(CONST_SQL_GET_MAIN_COMPANY)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_main_company_detail_from_ticker_us(self, ticker):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_MAIN_COMPANY = """SELECT * FROM maincompany WHERE ticker = '{TICKER}' LIMIT 1;""".format(TICKER=str(ticker))
            cur.execute(CONST_SQL_GET_MAIN_COMPANY)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_main_company_detail_from_ticker_yfinance(self, ticker_yfinance):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_MAIN_COMPANY = """SELECT * FROM maincompany WHERE ticker_yfinance = '{TICKER}' LIMIT 1;""".format(TICKER=str(ticker_yfinance))
            cur.execute(CONST_SQL_GET_MAIN_COMPANY)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_main_company_detail_from_main_company_id(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_MAIN_COMPANY = """SELECT * FROM maincompany WHERE id = {ID} LIMIT 1;"""
            query = CONST_SQL_GET_MAIN_COMPANY.format(ID=str(main_company_id))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()
