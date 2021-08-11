import db.db_access as access

import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class psql_webtraffic_pipeline_connector_db(object):
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
            CONST_SQL_GET_MAIN_COMP_NAME = 'SELECT * FROM maincompany'
            cur.execute(CONST_SQL_GET_MAIN_COMP_NAME)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
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

    def get_reported_sales_estimation(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_REPORTED_SALES = 'SELECT * FROM public.quarter_sales_estimation'
            cur.execute(CONST_SQL_GET_REPORTED_SALES)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            df['actual_sales'] = df['actual_sales'].astype(float)
            df['estimation'] = df['estimation'].astype(float)
            return df
        finally:
            cur.close()

    '''
    def get_historical_prices(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_HIST_PRICE = 'SELECT * FROM historical_prices'
            cur.execute(CONST_SQL_GET_HIST_PRICE)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        finally:
            cur.close()
    
    def get_historical_price_from_ticker(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_HIST_PRICE_FROM_TICKER = """SELECT * FROM historical_prices WHERE main_company_id = {MAIN_COMPANY_ID};"""
        query = CONST_SQL_GET_HIST_PRICE_FROM_TICKER.format(MAIN_COMPANY_ID=str(main_company_id))
        cur.execute(query)
        df = cur.fetchall()
        df = pd.DataFrame.from_records(df, columns=[x[0] for x in cur.description])
        df['close'] = df['close'].astype(float)
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['volume'] = df['volume'].astype(float)
        return df
    '''
    def get_webtraffic_all(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_WEB_VISIT_ALL = '''SELECT name, total_visits, date FROM public.all_traffic'''
            cur.execute(CONST_SQL_GET_WEB_VISIT_ALL)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        finally:
            cur.close()

    def get_webtraffic_by_main_company_id(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID = '''SELECT t.main_company_id, t.total_visits, t.date FROM public.all_traffic t WHERE main_company_id = {MAIN_COMPANY_ID}'''
            query = CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID.format(MAIN_COMPANY_ID=str(main_company_id))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except:
            return pd.DataFrame()
        finally:
            cur.close()

    def get_backtest_result_all(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID = """SELECT * FROM backtest_result WHERE format_type = 'all_result' AND source = 'webtraffic_trend' ORDER BY compute_datetime DESC LIMIT 1"""
            cur.execute(CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except:
            return pd.DataFrame()
        finally:
            cur.close()

    def get_backtest_result_per_main_company_id(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID = """SELECT * FROM backtest_result WHERE format_type = 'ticker' AND source = 'webtraffic_trend' AND main_company_id = {MAIN_COMPANY_ID} ORDER BY compute_datetime DESC LIMIT 1"""
            query = CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID.format(MAIN_COMPANY_ID=str(main_company_id))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except:
            return pd.DataFrame()
        finally:
            cur.close()


    def insert_backtest_result(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'backtest_result'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def refresh_materialised_view_all_traffic(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_REFRESH_ALL_TRAFFIC_MAT_VIEW = """REFRESH MATERIALIZED VIEW all_traffic;"""
            cur.execute(CONST_SQL_REFRESH_ALL_TRAFFIC_MAT_VIEW)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
