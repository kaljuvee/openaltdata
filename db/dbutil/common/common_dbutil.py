import db.db_access as access

import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class CommonConnectorDb(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user,
                               password=self.password)
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
            CONST_SQL_GET_MAIN_COMPANY = """SELECT * FROM maincompany WHERE ticker_bbg = '{TICKER}' LIMIT 1""".format(
                TICKER=str(ticker_bbg))
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

    def get_backtest_result_all(self, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID = """SELECT * FROM backtest_result WHERE format_type = 'all_result' AND source = '{SOURCE}' ORDER BY compute_datetime DESC LIMIT 1"""
            query = CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID.format(SOURCE=str(source))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except:
            return pd.DataFrame()
        finally:
            cur.close()

    def get_backtest_result_per_main_company_id(self, main_company_id, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID = """SELECT * FROM backtest_result WHERE format_type = 'ticker' AND source = '{SOURCE}' AND main_company_id = {MAIN_COMPANY_ID} ORDER BY compute_datetime DESC LIMIT 1"""
            query = CONST_SQL_GET_WEB_VISIT_MAIN_COMPANY_ID.format(SOURCE=str(source), MAIN_COMPANY_ID=str(main_company_id))
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

    def delete_old_backtest_result(self, table_name, timestamp):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            DELETE_SQL_OLD_BACKTEST_RESULT = """DELETE FROM {TABLE_NAME} WHERE compute_datetime <= '{TIMESTAMP}'"""
            query = DELETE_SQL_OLD_BACKTEST_RESULT.format(TABLE_NAME=str(table_name), TIMESTAMP=str(timestamp))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def vacuum_db(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_REFRESH_ALL_TRAFFIC_MAT_VIEW = """VACUUM FULL;"""
            cur.execute(CONST_SQL_REFRESH_ALL_TRAFFIC_MAT_VIEW)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
