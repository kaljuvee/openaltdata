import db.db_access as access

import psycopg2
from sqlalchemy import create_engine
import pandas as pd


class psql_keyword_connector_db(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_main_company(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_MAIN_COMP_NAME = 'SELECT * FROM maincompany'
        cur.execute(CONST_SQL_GET_MAIN_COMP_NAME)
        result = cur.fetchall()
        result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return result

    def get_company(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_COMPANY = """SELECT * FROM company"""
        cur.execute(CONST_SQL_GET_COMPANY)
        result = cur.fetchall()
        result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return result

    def get_main_company_info_details_from_main_company_id(self, main_company_id):
        engine = self.get_create_engine()
        query = """SELECT * FROM maincompany WHERE id = {MAIN_COMPANY_ID}""".format(MAIN_COMPANY_ID=str(main_company_id))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get_company_info_details_from_main_company_id(self, main_company_id):
        engine = self.get_create_engine()
        query = """SELECT * FROM company WHERE main_company_id = {MAIN_COMPANY_ID} AND is_parent_company = TRUE""".format(MAIN_COMPANY_ID=str(main_company_id))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get_google_trend_detail(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_COMP_GTREND_DETAIL = """SELECT id, main_company_id, google_trend_keyword, google_trend_url FROM company;"""
        cur.execute(CONST_SQL_GET_COMP_GTREND_DETAIL)
        result = cur.fetchall()
        result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return result

    def get_reported_sales_estimation(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_REPORTED_SALES = 'SELECT * FROM public.quarter_sales_estimation'
        cur.execute(CONST_SQL_GET_REPORTED_SALES)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        df['actual_sales'] = df['actual_sales'].astype(float)
        df['estimation'] = df['estimation'].astype(float)
        return df

    def get_google_trend_from_keyword(self, google_trend_url):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_GTREND_KEYWORD = """SELECT * FROM google_trend WHERE google_trend_url = '{URL}' ORDER BY compute_datetime desc LIMIT 1""".format(URL=str(google_trend_url))
        cur.execute(CONST_SQL_GET_GTREND_KEYWORD)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df

    def delete_old_google_trend(self, google_trend_url):
        cnx = self.get_psql_context()
        cursor = cnx.cursor()
        try:
            DELETE_GOOGLE_TREND = """DELETE FROM google_trend WHERE google_trend_url = '{URL}'"""
            query = DELETE_GOOGLE_TREND.format(URL=str(google_trend_url))
            cursor.execute(query)
            cnx.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Failed to insert record into Laptop table {}".format(error))

        finally:
            cursor.close()
            cnx.close()

    def insert_google_trend(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'google_trend'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_backtest_result(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'backtest_result'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_empty_company_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_UPDATE_EMPTY_COMPANY_TABLE = """UPDATE company SET google_trend_keyword = NULL WHERE google_trend_keyword ='';"""
            cur.execute(CONST_SQL_UPDATE_EMPTY_COMPANY_TABLE)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
