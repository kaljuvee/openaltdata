import psycopg2
import pandas as pd
import db.db_access as access
from datetime import timedelta, datetime
from sqlalchemy import create_engine


class RedditConnectorDB(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def db_check_existent_posts(self, s):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_CHECK_EXISTENT_POSTS = """SELECT id, post_id, comments, last_update_data FROM reddit_posts WHERE post_id = ANY (%s)"""

            cur.execute(CONST_SQL_CHECK_EXISTENT_POSTS, (list(s),))
            result = cur.fetchall()

            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            df = pd.DataFrame()
        finally:
            cur.close()
        return df

    def get_ticker_freq_from_to(self, start_datetime, end_datetime):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_CHECK_EXISTENT_POSTS = """SELECT * FROM reddit_ticker_analysis WHERE compute_datetime >= '{START}' AND compute_datetime <= '{END}'"""
            query = CONST_SQL_CHECK_EXISTENT_POSTS.format(START=str(start_datetime), END=str(end_datetime))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            df = pd.DataFrame()
        finally:
            cur.close()
        return df

    def insert_reddit_post(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'reddit_posts'

            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_reddit_ticker_analysis(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'reddit_ticker_analysis'

            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_reddit_post(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['last_update_data', 'comments', 'last_update_datetime', 'id']]
        try:
            CONST_SQL_UPDATE_SENTIMENT_DATE = 'UPDATE reddit_posts SET last_update_data=%s, comments=%s, last_update_datetime=%s WHERE id = %s'
            cur.executemany(CONST_SQL_UPDATE_SENTIMENT_DATE, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
        return
