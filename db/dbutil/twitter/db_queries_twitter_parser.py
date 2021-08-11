import psycopg2
import pandas as pd
import db.db_access as access
from datetime import timedelta, datetime
from sqlalchemy import create_engine


""" part for the normal keyword twitter pipeline"""
CONST_SQL_GET_MAIN_COMPANY = 'SELECT * FROM maincompany'
CONST_SQL_UPDATE_EMPTY_COMPANY_TABLE = "UPDATE company SET twitter_keyword = NULL WHERE twitter_keyword ='';"

CONST_SQL_LAST_DATE_TWEET = 'SELECT MAX(date) FROM tweet WHERE company_id = {COMPANY_ID};'
CONST_SQL_GET_TWEET_LIST = 'Select id from tweet'
CONST_SQL_GET_TWEET_LIST_FOR_SENTIMENT = "SELECT id, tweet, date, timezone FROM tweet WHERE date_utc is null and timezone <> 'UTC' limit 1000"
CONST_SQL_GET_TWEET_SPECIFIC = 'Select * from tweet WHERE id = {TWEET_ID}'
CONST_SQL_UPDATE_SENTIMENT_DATE = 'UPDATE tweet SET date_utc=%s, sentiment_score_textblob=%s, sentiment_score_vader=%s WHERE id = %s'
CONST_SQL_MIN_DATE_TWEET = 'SELECT MIN(date) FROM tweet WHERE company_id = {COMPANY_ID};'
CONST_SQL_UPDATE_UTC_TIMEZONE = """UPDATE tweet SET timezone = '+0000' WHERE timezone = 'UTC';"""
CONST_SQL_GET_TICKER_WITH_COMPANY_ID = 'SELECT c.id, c.main_company_id, m.ticker FROM company c LEFT JOIN maincompany m ON c.main_company_id = m.id'
CONST_SQL_GET_TWEET_SPECIFIC_DATE = """Select * from tweet WHERE company_id = {COMPANY_ID} AND date >= '{DATE}' AND date < '{DATE2}'"""
CONST_SQL_GET_ID_LAST_TWEET = """SELECT id FROM tweet WHERE company_id = {COMPANY_ID} AND date = '{DATE}' """
CONST_SQL_GET_LIST_DATE = """Select to_char(t.date, 'yyyy-mm-dd'::text) AS date from tweet t WHERE company_id = {COMPANY_ID} group by to_char(t.date, 'yyyy-mm-dd'::text) order by date"""

"""part for the cashtag twitter pipeline"""
CONST_SQL_GET_MAIN_COMPANY = 'SELECT * FROM maincompany'
CONST_SQL_UPDATE_EMPTY_COMPANY_TABLE_CASHTAG = "UPDATE company SET twitter_cashtag = NULL WHERE twitter_cashtag ='';"
CONST_SQL_LAST_DATE_TWEET_CASHTAG = 'SELECT MAX(date) FROM tweet_cashtag WHERE company_id = {COMPANY_ID};'
CONST_SQL_MIN_DATE_TWEET_CASHTAG = 'SELECT MIN(date) FROM tweet_cashtag WHERE company_id = {COMPANY_ID};'
CONST_SQL_GET_TWEET_LIST_CASHTAG = 'Select id from tweet'
CONST_SQL_GET_TWEET_LIST_FOR_SENTIMENT_CASHTAG = "SELECT id, tweet, date, timezone FROM tweet_cashtag WHERE date_utc is null and timezone <> 'UTC' limit 1000"
CONST_SQL_GET_TWEET_SPECIFIC_CASHTAG = 'Select * from tweet_cashtag WHERE id = {TWEET_ID}'
CONST_SQL_UPDATE_SENTIMENT_DATE_CASHTAG = 'UPDATE tweet_cashtag SET date_utc=%s, sentiment_score_textblob=%s, sentiment_score_vader=%s WHERE id = %s'
CONST_SQL_UPDATE_UTC_TIMEZONE_CASHTAG = """UPDATE tweet_cashtag SET timezone = '+0000' WHERE timezone = 'UTC';"""
CONST_SQL_GET_TWEET_SPECIFIC_DATE_CASHTAG = """Select * from tweet_cashtag WHERE company_id = {COMPANY_ID} AND date >= '{DATE}' AND date < '{DATE2}'"""
CONST_SQL_GET_ID_LAST_TWEET_CASHTAG = """SELECT id FROM tweet_cashtag WHERE company_id = {COMPANY_ID} AND date = '{DATE}'"""
CONST_SQL_GET_LIST_DATE_CASGTAG = """Select to_char(t.date, 'yyyy-mm-dd'::text) AS date from tweet_cashtag t WHERE company_id = {COMPANY_ID} group by to_char(t.date, 'yyyy-mm-dd'::text) order by date"""

#for daily twitter webservice
CONST_SQL_GET_QUARTER_ENDS = """SELECT * FROM "public"."parsing_twitter_cashtag" t WHERE t.search = {CASHTAG}  AND  TO_CHAR(t.date, 'yyyy-mm-dd')= + {DATE}"""

"""part for the old parser with more columns"""
CONST_SQL_INSERT_TWEET = """
INSERT INTO tweet(tweet_id, conversation_id, date, timezone, tweet, hashtags, cashtags, user_id_str, username, nlikes,
nreplies, nretweets, quote_url, reply_to, date_update, company_id, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
CONST_SQL_INSERT_TWEET_CASHTAG ="""
INSERT INTO tweet_cashtag(tweet_id, conversation_id, date, timezone, tweet, hashtags, cashtags, user_id_str, username, nlikes,
nreplies, nretweets, quote_url, reply_to, date_update, company_id, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

""" this part is for the tweet long parsing"""

CONST_SQL_LAST_DATE_TWEET_LONG = 'SELECT MAX(date) FROM parsing_twitter WHERE company_id = {COMPANY_ID};'
CONST_SQL_ALL_CASHTAG_TWEET = 'SELECT * FROM parsing_twitter_cashtag LIMIT 1000'
DELETE_SQL_ALLCASHTAG_TWEET = 'DELETE FROM parsing_twitter_cashtag WHERE tweet_id = {TWEET_ID};'
CONST_SQL_LAST_DATE_TWEET_CASHTAG_LONG = 'SELECT MAX(date) FROM parsing_twitter_cashtag WHERE company_id = {COMPANY_ID};'
CONST_SQL_INSERT_PARSING_TWITTER_LONG = """
INSERT INTO parsing_twitter(tweet_id, conversation_id, created_at, date, timezone, place, tweet, hashtags, cashtags, user_id, user_id_str, username, name, day, hour, link, retweet, nlikes
    , nreplies, nretweets, quote_url, search, near, geo, source, user_rt_id, user_rt, retweet_id, reply_to, retweet_date, translate, trans_src, trans_dest, date_update, company_id) VALUES (%s
    , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
CONST_SQL_INSERT_PARSING_TWITTER_CASHTAG_LONG = """
INSERT INTO parsing_twitter_cashtag(tweet_id, conversation_id, created_at, date, timezone, place, tweet, hashtags, cashtags, user_id, user_id_str, username, name, day, hour, link, retweet, nlikes
    , nreplies, nretweets, quote_url, search, near, geo, source, user_rt_id, user_rt, retweet_id, reply_to, retweet_date, translate, trans_src, trans_dest, date_update, company_id) VALUES (%s
    , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


CONST_SQL_REFRESH_KEYWORD_MAT_VIEW = """REFRESH MATERIALIZED VIEW day_keyword_materialised;"""
CONST_SQL_REFRESH_KEYWORD_MAT_VIEW_WITH_FILTER = """REFRESH MATERIALIZED VIEW day_keyword_like_filter_materialised;"""
CONST_SQL_REFRESH_CASHTAG_MAT_VIEW = """REFRESH MATERIALIZED VIEW day_cashtag_materialised;"""
CONST_SQL_REFRESH_CASHTAG_MAT_VIEW_WITH_FILTER = """REFRESH MATERIALIZED VIEW day_CASHTAG_like_filter_materialised;"""

CONST_SQL_REMOVE_DUPLICATES = """DELETE FROM tweet a USING tweet b WHERE a.id < b.id AND a.tweet_id = b.tweet_id AND a.company_id = b.company_id;"""
CONST_SQL_REMOVE_DUPLICATES_CASHTAG = """DELETE FROM tweet_cashtag a USING tweet b WHERE a.id < b.id AND a.tweet_id = b.tweet_id AND a.company_id = b.company_id;"""
CONST_SQL_REMOVE_OLD_TWEET = """DELETE FROM tweet WHERE date <='{DATE}' """
CONST_SQL_REMOVE_OLD_TWEET_CASHTAG = """DELETE FROM tweet_cashtag WHERE date <='{DATE}' """


def first_column(array_2d):
    return list(zip(*array_2d))[0]


def get_ticker_from_company_id():
    host, port, database, user, password = access.postgre_access_google_cloud()
    cnx = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
    cur = cnx.cursor()
    cur.execute(CONST_SQL_GET_TICKER_WITH_COMPANY_ID)
    result = cur.fetchall()
    result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
    return result


class Twitter_keyword_connector_db(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

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

    def get_last_date_tweet(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_LAST_DATE_TWEET.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_min_date_tweet(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_MIN_DATE_TWEET.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_last_date_tweet_cashtag(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_LAST_DATE_TWEET_CASHTAG.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_tweets_specific_date(self, company_id, date):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            date2 = date + timedelta(days=1)
            query = CONST_SQL_GET_TWEET_SPECIFIC_DATE.format(COMPANY_ID=str(company_id), DATE=str(date), DATE2=str(date2))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def last_id_from_last_tweet(self, company_id, last_date):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_ID_LAST_TWEET.format(COMPANY_ID=str(company_id), DATE=str(last_date))
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_parsing_tweet_old(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            df = df[['tweet_id', 'conversation_id', 'date', 'timezone', 'tweet', 'hashtags', 'cashtags',
                     'user_id_str', 'username', 'nlikes', 'nreplies', 'nretweets', 'quote_url', 'reply_to',
                     'date_update', 'company_id', 'link']]

            df['company_id'] = df['company_id'].astype(int)
            df['nlikes'] = df['nlikes'].astype(int)
            df['nreplies'] = df['nreplies'].astype(int)
            df['nretweets'] = df['nretweets'].astype(int)

            df['hashtags'] = df['hashtags'].astype(str)
            df['cashtags'] = df['cashtags'].astype(str)
            df['reply_to'] = df['reply_to'].astype(str)
            df['link'] = df['link'].astype(str)

            cur.executemany(CONST_SQL_INSERT_TWEET, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_parsing_tweet(self, df):
        engine = self.get_create_engine()
        try:
            df = df[['tweet_id', 'conversation_id', 'date', 'timezone', 'tweet', 'hashtags', 'cashtags',
                     'user_id_str', 'username', 'nlikes', 'nreplies', 'nretweets', 'quote_url', 'reply_to',
                     'date_update', 'company_id', 'link', 'is_spam']]

            df['company_id'] = df['company_id'].astype(int)
            df['nlikes'] = df['nlikes'].astype(int)
            df['nreplies'] = df['nreplies'].astype(int)
            df['nretweets'] = df['nretweets'].astype(int)

            df['hashtags'] = df['hashtags'].astype(str)
            df['cashtags'] = df['cashtags'].astype(str)
            df['reply_to'] = df['reply_to'].astype(str)
            df['link'] = df['link'].astype(str)

            table_name = 'tweet'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_tweet_id_list(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_TWEET_LIST
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_tweet_id_list_for_sentiment(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_TWEET_LIST_FOR_SENTIMENT
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_specific_tweet(self, tweet_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_TWEET_SPECIFIC.format(TWEET_ID=str(tweet_id))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_all_dates_from_ticker(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_LIST_DATE.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            df['date'] = df['date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d').date(), list(df['date']))
            return df
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_sentiment_date(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['date_utc', 'sentiment_score_textblob', 'sentiment_score_vader', 'id']]
        try:
            cur.executemany(CONST_SQL_UPDATE_SENTIMENT_DATE, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_utc_timezone(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_UPDATE_UTC_TIMEZONE)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_empty_company_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_UPDATE_EMPTY_COMPANY_TABLE)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def refresh_materialised_view_day(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_REFRESH_KEYWORD_MAT_VIEW)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def refresh_materialised_view_day_with_filter(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_REFRESH_KEYWORD_MAT_VIEW_WITH_FILTER)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_duplicates(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_REMOVE_DUPLICATES)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_old_tweet(self, timestamp):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_REMOVE_OLD_TWEET.format(DATE=str(timestamp))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_other_data(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'twitter_materialised_views'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


class Twitter_cashtag_connector_db(object):
    """
    the same object as above but for the twitter cashtag pipeline
    """
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
            cur.execute(CONST_SQL_GET_MAIN_COMPANY)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_twitter_detail(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_TWITTER_DET = 'SELECT * FROM twitter_detail'
        cur.execute(CONST_SQL_GET_TWITTER_DET)
        result = cur.fetchall()
        result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return result

    def get_last_date_tweet(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_LAST_DATE_TWEET_CASHTAG.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            return result[0][0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_min_date_tweet(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_MIN_DATE_TWEET_CASHTAG.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result[0][0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_tweets_specific_date(self, company_id, date):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            date2 = date + timedelta(days=1)
            query = CONST_SQL_GET_TWEET_SPECIFIC_DATE_CASHTAG.format(COMPANY_ID=str(company_id), DATE=str(date), DATE2=str(date2))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_all_dates_from_ticker(self, company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_LIST_DATE_CASGTAG.format(COMPANY_ID=str(company_id))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            df['date'] = df['date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d').date(), list(df['date']))
            return df
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_parsing_tweet_old(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cnx = self.get_psql_context()
            cur = cnx.cursor()

            df = df[['tweet_id', 'conversation_id', 'date', 'timezone', 'tweet', 'hashtags', 'cashtags',
                     'user_id_str', 'username', 'nlikes', 'nreplies', 'nretweets', 'quote_url', 'reply_to',
                     'date_update', 'company_id', 'link']]

            df['company_id'] = df['company_id'].astype(int)
            df['nlikes'] = df['nlikes'].astype(int)
            df['nreplies'] = df['nreplies'].astype(int)
            df['nretweets'] = df['nretweets'].astype(int)

            df['hashtags'] = df['hashtags'].astype(str)
            df['cashtags'] = df['cashtags'].astype(str)
            df['reply_to'] = df['reply_to'].astype(str)
            df['link'] = df['link'].astype(str)

            cur.executemany(CONST_SQL_INSERT_TWEET_CASHTAG, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_parsing_tweet(self, df):
        engine = self.get_create_engine()
        try:
            df = df[['tweet_id', 'conversation_id', 'date', 'timezone', 'tweet', 'hashtags', 'cashtags',
                     'user_id_str', 'username', 'nlikes', 'nreplies', 'nretweets', 'quote_url', 'reply_to',
                     'date_update', 'company_id', 'link', 'is_spam']]

            df['company_id'] = df['company_id'].astype(int)
            df['nlikes'] = df['nlikes'].astype(int)
            df['nreplies'] = df['nreplies'].astype(int)
            df['nretweets'] = df['nretweets'].astype(int)

            df['hashtags'] = df['hashtags'].astype(str)
            df['cashtags'] = df['cashtags'].astype(str)
            df['reply_to'] = df['reply_to'].astype(str)
            df['link'] = df['link'].astype(str)

            table_name = 'tweet_cashtag'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_tweet_id_list(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        query = CONST_SQL_GET_TWEET_LIST_CASHTAG
        cur.execute(query)
        result = cur.fetchall()
        result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return result

    def get_tweet_id_list_for_sentiment(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_TWEET_LIST_FOR_SENTIMENT_CASHTAG
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def get_specific_tweet(self, tweet_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_GET_TWEET_SPECIFIC_CASHTAG.format(TWEET_ID=str(tweet_id))
            cur.execute(query)
            result = cur.fetchall()
            result = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_sentiment_date(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['date_utc', 'sentiment_score_textblob', 'sentiment_score_vader', 'id']]
        try:
            cur.executemany(CONST_SQL_UPDATE_SENTIMENT_DATE_CASHTAG, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_utc_timezone(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_UPDATE_UTC_TIMEZONE_CASHTAG)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_empty_company_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_UPDATE_EMPTY_COMPANY_TABLE_CASHTAG)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def refresh_materialised_view_day(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_REFRESH_CASHTAG_MAT_VIEW)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def refresh_materialised_view_day_with_filter(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_REFRESH_CASHTAG_MAT_VIEW_WITH_FILTER)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_duplicates(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_REMOVE_DUPLICATES_CASHTAG)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_old_tweet(self, timestamp):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = CONST_SQL_REMOVE_OLD_TWEET_CASHTAG.format(DATE=str(timestamp))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_other_data(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'twitter_materialised_views'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
