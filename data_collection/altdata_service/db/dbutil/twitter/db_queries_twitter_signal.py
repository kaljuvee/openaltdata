import psycopg2
import pandas as pd
import db.db_access as access


CONST_SQL_GET_TWITTER_DET = 'SELECT id, main_company_id, twitter_keyword, twitter_cashtag, twitter_url, is_parent_company FROM company'
CONST_SQL_GET_MAIN_COMPANY = 'SELECT * FROM maincompany'
CONST_SQL_GET_COMPANY_DETAIL = 'SELECT * FROM company_detail'
CONST_SQL_GET_MAT_VIEW_KEYWORD = 'SELECT * FROM public.day_keyword_materialised'
CONST_SQL_GET_MAT_VIEW_CASHTAG = 'SELECT * FROM public.day_cashtag_materialised'
CONST_SQL_LAST_DATE_TWEET = """SELECT MAX(date_utc) FROM {TABLE} WHERE company_id = '{COMPANY_ID}';"""
CONST_SQL_GET_MAT_VIEW_FOR_COMPANY = """SELECT """


# for daily twitter webservice
CONST_SQL_GET_TWEETS_BY_CASHTAG = """SELECT * FROM "public"."parsing_twitter_cashtag" t WHERE t.search = {CASHTAG}  AND  TO_CHAR(t.date, 'yyyy-mm-dd')= + {DATE}"""


class TwitterConnectorDbSignal(object):

    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user,
                               password=self.password)
        return cnx

    def get_twitter_detail(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_TWITTER_DET = 'SELECT * FROM twitter_detail'
            cur.execute(CONST_SQL_GET_TWITTER_DET)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_last_date_tweet(self, company_id, table_name):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        query = CONST_SQL_LAST_DATE_TWEET.format(TABLE=str(table_name), COMPANY_ID=str(company_id))
        cur.execute(query)
        result = cur.fetchall()
        return result[0][0]

    def get_main_company(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_MAIN_COMPANY)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_company_detail(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_COMPANY_DETAIL)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_link_tweet_from_period_range(self, company_id, date_utc, table_name):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_LINK_LIKES_PERIOD_RANGE = """SELECT tweet_id, link, tweet, nlikes, sentiment_score_vader, cashtags
            FROM {TABLE} WHERE is_spam is False AND company_id = '{COMPANY_ID}' AND date_utc BETWEEN '{DATE_UTC}' AND '{DATE_UTC_2} 23:59:59.997';"""
            query = CONST_SQL_GET_LINK_LIKES_PERIOD_RANGE.format(TABLE=str(table_name), COMPANY_ID=str(company_id), DATE_UTC=str(date_utc), DATE_UTC_2=str(date_utc))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_more_tweet(self, company_id, table_name):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_LINK_LIKES_PERIOD_RANGE = """SELECT tweet_id, link, tweet, nlikes, sentiment_score_vader, cashtags
                        FROM {TABLE} WHERE is_spam is False AND company_id = '{COMPANY_ID}' AND nlikes >=1 ORDER BY date_utc DESC LIMIT 40"""

            query = CONST_SQL_GET_LINK_LIKES_PERIOD_RANGE.format(TABLE=str(table_name), COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_materialised_view_keyword(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_MAT_VIEW_KEYWORD)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_materialised_view_cashtag(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_MAT_VIEW_CASHTAG)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_materialised_view_for_company_id(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_MAT_VIEW_FOR_COMPANY)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
