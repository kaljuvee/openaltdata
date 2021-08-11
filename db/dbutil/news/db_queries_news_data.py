import psycopg2
import pandas as pd
import db.db_access as access
from sqlalchemy import create_engine


class psql_db_news_data_gcp(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud_news()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_entity_company(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_ENTITY_COMPANY = 'SELECT * FROM entity_company'
            cur.execute(CONST_SQL_GET_ENTITY_COMPANY)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_news_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_NEWS_TABLE = 'SELECT ticker FROM news WHERE sector is NULL'
            cur.execute(CONST_SQL_GET_NEWS_TABLE)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_entire_news_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_ENTIRE_NEWS_TABLE = 'SELECT * FROM news'
            cur.execute(CONST_SQL_GET_ENTIRE_NEWS_TABLE)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def update_entity_company(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            UPDATE_ENTITY_COMPANY = 'UPDATE entity_company SET market_cap = %s, sector = %s, sub_sector = %s, ticker = %s, ticker_eod = %s WHERE ric=%s'
            df = df[['market_cap', 'sector', 'sub_sector', 'ticker', 'ticker_eod', 'ric']]
            cur.executemany(UPDATE_ENTITY_COMPANY, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_new_table(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            UPDATE_NEWS = 'UPDATE news SET market_cap = %s, sector = %s, sub_sector = %s, ticker = %s WHERE ticker = %s'
            df = df[['market_cap', 'sector', 'sub_sector', 'ticker_normal', 'ticker']]
            cur.executemany(UPDATE_NEWS, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_into_news_table(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'news'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_from_news_table(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            DELETE_ROW_BY_NEWS_ID = 'DELETE FROM news WHERE news_id=%s'
            df = df[['news_id']]
            cur.executemany(DELETE_ROW_BY_NEWS_ID, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_news_item_entity_company_combined(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            SQL_GET_NEWS_ITEM_AND_ENTITY_CO_COMBINED = 'SELECT ni.*, co.* FROM news_item ni, entity_company co WHERE ni.news_item_id = co.news_item_id'
            cur.execute(SQL_GET_NEWS_ITEM_AND_ENTITY_CO_COMBINED)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def select_content_that_does_not_exist_in_news(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            SELECT_CONTENT_THAT_DOES_NOT_EXIST_IN_NEWS = 'SELECT * FROM news_item ni where ni.link NOT IN ( SELECT n2.link FROM news n2 )'
            cur.execute(SELECT_CONTENT_THAT_DOES_NOT_EXIST_IN_NEWS)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def delete_test_data_from_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            DELETE_TEST_DATA = "DELETE FROM news WHERE title like '%Test Title%'"
            cur.execute(DELETE_TEST_DATA)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()


if __name__ == "__main__":
    print('starting test db')
    conn = psql_db_news_data_gcp()
