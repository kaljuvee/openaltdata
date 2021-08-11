import psycopg2
import pandas as pd
from sqlalchemy import create_engine

import db.db_access as access


INST_SQL_SIGNAL_STRENGTH = 'INSERT INTO signal_strength (main_company_id, ticker, r_square, source, compute_datetime) VALUES(%s, %s, %s, %s, %s)'
CONST_SQL_INSERT_ANNOUNCEMENT_CALENDAR = """INSERT INTO announcement_calendar (compute_datetime, calendar, source) VALUES (%s, %s, %s)"""
CONST_INST_SQL_TWITTER_SIGNAL = """INSERT INTO twitter_trading_signal (ticker, signal_date, compute_datetime, signal_json, sector, 
sub_sector, market_cap, company_link, tweet_link, signal_decision, sentiment, company_name, tweet_text, top_tweets, main_company_id) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

DELETE_SQL_MODEL_FORECAST_ESTIMATION_WEB = """DELETE FROM model_forecast_sales_estimation_web_traffic WHERE ticker = '{TICKER}' and source = '{SOURCE}'"""
DELETE_SQL_SIGNAL_STRENGTH = """DELETE FROM signal_strength WHERE ticker = '{TICKER}' and source = '{SOURCE}'"""


class psql_db_altcap_api_connector(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud_altcap_api()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_signal_chart_data(self, source, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_SIGNAL_GRAPH = """SELECT data_json FROM model_forecast_sales_estimation_web_traffic WHERE 
            main_company_id='{MAIN_COMPANY_ID}' and source='{SOURCE}' order by compute_datetime desc limit 1;"""

            query = CONST_SQL_GET_SIGNAL_GRAPH.format(MAIN_COMPANY_ID=str(main_company_id), SOURCE=str(source))
            cur.execute(query)
            result = cur.fetchall()

            if result == []:
                return pd.DataFrame()
            else:
                return result[0][0]

        finally:
            cur.close()

    def get_other_data(self, source, ticker):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_OTHER_DATA = """SELECT * FROM other_data WHERE main_company_id='{MAIN_COMPANY_ID}' and source='{SOURCE}' order by compute_datetime desc limit 1;"""
            query = CONST_SQL_GET_OTHER_DATA.format(TICKER=str(ticker), SOURCE=str(source))
            cur.execute(query)
            result = cur.fetchall()
            return result[0][5]
        finally:
            cur.close()

    def get_signal_strength(self, source, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_SIGNAL_STRENGTH = """SELECT * FROM signal_strength WHERE main_company_id='{MAIN_COMPANY_ID}' and source='{SOURCE}' order by compute_datetime desc limit 1;"""
            query = CONST_SQL_GET_SIGNAL_STRENGTH.format(MAIN_COMPANY_ID=str(main_company_id), SOURCE=str(source))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_calendar_db(self, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_LAST_UPDATED_CALENDAR = """SELECT calendar FROM announcement_calendar where source='{SOURCE}' order by compute_datetime desc limit 1;"""
            query = CONST_SQL_GET_LAST_UPDATED_CALENDAR.format(SOURCE=str(source))
            cur.execute(query)
            return cur.fetchall()[0][0]
        finally:
            cur.close()

    def get_calendar_with_history_db(self, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            result = []

            CONST_SQL_GET_LAST_UPDATED_CALENDAR_WITH_HIST = """SELECT calendar FROM announcement_calendar where source='{SOURCE}' order by compute_datetime desc limit 20;"""
            query = CONST_SQL_GET_LAST_UPDATED_CALENDAR_WITH_HIST.format(SOURCE=str(source))
            cur.execute(query)
            result_db = cur.fetchall()
            # join the lists together
            for i in range(len(result_db) - 1):
                result += result_db[i][0]
            return result
        finally:
            cur.close()

    def get_twitter_sentiment(self, cut_date):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_TWITTER_SENTIMENT = """
                select * 
                from twitter_trading_signal
                join (select max(compute_datetime) as max_tmst from twitter_trading_signal) tbl
                on tbl.max_tmst = twitter_trading_signal.compute_datetime
                where ticker is not NULL AND signal_date >= '{CUTOFF_DATE}'
                order by compute_datetime desc; 
                """

        query = CONST_SQL_GET_TWITTER_SENTIMENT.format(CUTOFF_DATE=cut_date)
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df

    def get_twitter_sentiment_ticker(self, main_company_id, cut_date):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_TWITTER_SENTIMENT_TICKER = """
                select *
                from twitter_trading_signal
                join (select max(compute_datetime) as max_tmst from twitter_trading_signal) tbl
                on tbl.max_tmst = twitter_trading_signal.compute_datetime
                where main_company_id = '{MAIN_COMPANY_ID}' AND signal_date >= '{CUTOFF_DATE}'
                order by compute_datetime desc;
                """

        query = CONST_SQL_GET_TWITTER_SENTIMENT_TICKER.format(MAIN_COMPANY_ID=str(main_company_id), CUTOFF_DATE=cut_date)
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df.loc[0]

    def get_twitter_sentiment_yesterday(self, today, yesterday):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_TWITTER_SENTIMENT_YESTERDAY = """SELECT * FROM twitter_trading_signal
        WHERE ticker is not NULL AND compute_datetime >='{YESTERDAY}' AND compute_datetime <'{TODAY}' ORDER BY compute_datetime DESC"""

        query = CONST_SQL_GET_TWITTER_SENTIMENT_YESTERDAY.format(YESTERDAY=str(yesterday), TODAY=str(today))
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df.drop_duplicates(subset='ticker')

    def get_twitter_trending_stock_sentiment(self, cut_date):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_TWITTER_SENTIMENT = """
                select main_company_id, ticker, company_name, z_score_sentiment, signal_strength_sentiment, signal_decision_sentiment, z_score_number, signal_strength_number, signal_decision_number,
                number_tweets, price_open, price_close, price_high, price_low, price_change, price_change_pct, company_link
                from twitter_trading_signal
                join (select max(compute_datetime) as max_tmst from twitter_trading_signal) tbl
                on tbl.max_tmst = twitter_trading_signal.compute_datetime
                where ticker is not NULL AND signal_date >= '{CUTOFF_DATE}'
                order by compute_datetime desc; 
                """

        query = CONST_SQL_GET_TWITTER_SENTIMENT.format(CUTOFF_DATE=cut_date)
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df

    def get_twitter_trending_stock_yesterday(self, today, yesterday):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_TWITTER_SENTIMENT_YESTERDAY = """SELECT main_company_id, ticker, company_name, z_score_sentiment, signal_strength_sentiment, signal_decision_sentiment, z_score_number,
        signal_strength_number, signal_decision_number, number_tweets, price_open, price_close, price_high, price_low, price_change, price_change_pct, company_link 
        FROM twitter_trading_signal
        WHERE ticker is not NULL AND compute_datetime >='{YESTERDAY}' AND compute_datetime <'{TODAY}' ORDER BY compute_datetime DESC"""

        query = CONST_SQL_GET_TWITTER_SENTIMENT_YESTERDAY.format(YESTERDAY=str(yesterday), TODAY=str(today))
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df

    def get_twitter_sentiment_ticker_yesterday(self, main_company_id, today, yesterday):
        cnx = self.get_psql_context()
        cur = cnx.cursor()

        CONST_SQL_GET_TWITTER_SENTIMENT_YESTERDAY_TICKER = """SELECT * from twitter_trading_signal 
        where main_company_id = '{MAIN_COMPANY_ID}' AND compute_datetime >='{YESTERDAY}' AND compute_datetime <'{TODAY}' ORDER BY compute_datetime DESC"""


        query = CONST_SQL_GET_TWITTER_SENTIMENT_YESTERDAY_TICKER.format(MAIN_COMPANY_ID=str(main_company_id), YESTERDAY=str(yesterday), TODAY=str(today))
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df.loc[0]

    def insert_model_forecast_sales_estimation_web_traffic(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            df = df[['main_company_id', 'ticker', 'source', 'data_json', 'compute_datetime']]

            INST_SQL_MODEL_FORECAST_ESTIMATION_WEB = """INSERT INTO model_forecast_sales_estimation_web_traffic (main_company_id, ticker, source, data_json, compute_datetime)
            VALUES (%s, %s, %s, %s, %s)"""

            cur.executemany(INST_SQL_MODEL_FORECAST_ESTIMATION_WEB, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_signal_strength(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'signal_strength'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_calendar_db(self, timestamp, announcement_calendar_json, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_INSERT_ANNOUNCEMENT_CALENDAR, (timestamp, announcement_calendar_json, source))
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_twitter_trading_signal(self, df):
        """
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            df = df[['ticker', 'signal_date', 'compute_datetime', 'signal_json', 'sector', 'sub_sector', 'market_cap',
                     'company_link', 'tweet_link', 'signal_decision', 'sentiment', 'company_name', 'tweet_text', 'top_tweets', 'main_company_id']]
            cur.executemany(CONST_INST_SQL_TWITTER_SIGNAL, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
        """
        engine = self.get_create_engine()
        try:
            table_name = 'twitter_trading_signal'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_other_data(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'other_data'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_model_forecast_sales_estimation_web_traffic(self, ticker, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = DELETE_SQL_MODEL_FORECAST_ESTIMATION_WEB.format(TICKER=str(ticker), SOURCE=str(source))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_signal_strength(self, ticker, source):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = DELETE_SQL_SIGNAL_STRENGTH.format(TICKER=str(ticker), SOURCE=str(source))
            cur.execute(query)
            cnx.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            cur.close()

    def run_query_row_json(self, query):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        cur.execute(query)
        colnames = [desc[0] for desc in cur.description]
        table = cur.fetchall()
        row_oriented_table = []
        for elem in table:
            row_dict = {}
            for key, value in zip(colnames, elem):
                row_dict[key] = value
            row_oriented_table.append(row_dict)
        return row_oriented_table

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