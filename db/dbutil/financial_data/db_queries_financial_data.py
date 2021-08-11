import psycopg2
import pandas as pd
import db.db_access as access
from sqlalchemy import create_engine
from datetime import datetime
from data_collection.financial_service.common_objects_functions.arrange_historical_prices import arrange_historical_price


class psql_db_financial_data_gcp(object):
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

    def get_company_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_COMPANY = 'SELECT * FROM company'
            cur.execute(CONST_SQL_GET_COMPANY)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_reported_sales(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_REPORTED_SALES = 'SELECT * FROM reported_sales'
            cur.execute(CONST_SQL_GET_REPORTED_SALES)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_reported_sales_from_main_company_id(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_REPORTED_SALES_FROM_MAIN_COMPANY = """SELECT * FROM reported_sales WHERE main_company_id = {ID} ORDER BY end_quarter_date ASC"""
            query = CONST_SQL_GET_REPORTED_SALES_FROM_MAIN_COMPANY.format(ID=str(main_company_id))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_historical_price_from_ticker(self, ticker):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_HIST_PRICE_FROM_TICKER = """SELECT price_json FROM historical_prices_cached h WHERE ticker = '{TICKER}'
        and compute_datetime >= (select max(date_trunc('day', h.compute_datetime)) as start_day FROM historical_prices_cached h WHERE ticker = '{TICKER}');"""

        query = CONST_SQL_GET_HIST_PRICE_FROM_TICKER.format(TICKER=str(ticker))
        cur.execute(query)
        df = cur.fetchall()
        df = pd.DataFrame.from_records(df, columns=[x[0] for x in cur.description])

        if df.empty:
            return df
        # filter to take only the series that has the more data, meaning more historical dates for our process
        df['count'] = df['price_json'].apply(lambda x: len(x))
        result = pd.DataFrame(df[df['count'] == max(df['count'])].reset_index(drop=True).loc[0]['price_json'])
        result['date'] = result['date'].map(lambda x: datetime.fromtimestamp(x / 1000).date(), list(result['date']))
        return result

    def get_historical_price(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_HIST_PRICE = 'SELECT * FROM historical_prices'
        cur.execute(CONST_SQL_GET_HIST_PRICE)
        df = cur.fetchall()
        df = pd.DataFrame.from_records(df, columns=[x[0] for x in cur.description])
        df['close'] = df['close'].astype(float)
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['volume'] = df['volume'].astype(float)
        return df

    def get_historical_price_from_main_company_id(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_HIST_PRICE_FROM_MAIN_COMP_ID = """SELECT * FROM historical_prices WHERE main_company_id = {MAIN_COMPANY_ID}"""

        query = CONST_SQL_GET_HIST_PRICE_FROM_MAIN_COMP_ID.format(MAIN_COMPANY_ID=str(main_company_id))
        cur.execute(query)
        df = cur.fetchall()
        df = pd.DataFrame.from_records(df, columns=[x[0] for x in cur.description])
        df['close'] = df['close'].astype(float)
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['volume'] = df['volume'].astype(float)
        return df

    def get_historical_price_cached(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_HIST_PRICE_CACHED = """select * from historical_prices_cached WHERE main_company_id = {MAIN_COMPANY_ID} order by compute_datetime DESC"""
        query = CONST_SQL_GET_HIST_PRICE_CACHED.format(MAIN_COMPANY_ID=str(main_company_id))
        cur.execute(query)
        df = cur.fetchall()
        df = pd.DataFrame.from_records(df, columns=[x[0] for x in cur.description])
        return df

    def get_last_2_hist_prices(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        CONST_SQL_GET_LAST_2_HISTORICAL_PRICES = """SELECT * FROM historical_prices WHERE main_company_id='{MAIN_COMPANY_ID}' ORDER BY date DESC LIMIT 2"""
        query = CONST_SQL_GET_LAST_2_HISTORICAL_PRICES.format(MAIN_COMPANY_ID=str(main_company_id))
        cur.execute(query)
        result = cur.fetchall()
        df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
        return df.sort_values(by='date', ascending=True)

    def get_daily_sales_estimation(self):
        """
        Returns reported sales for all companies.
        Among the column names the column "group" actually means quarter
        :param company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_DAILY_ESTIMATION = 'SELECT * FROM daily_sales_estimation;'
            cur.execute(CONST_SQL_GET_DAILY_ESTIMATION)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_daily_sales_estimation_per_main_company_id(self, main_company_id):
        """
        Returns reported sales for all companies.
        Among the column names the column "group" actually means quarter
        :param main_company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_GET_DAILY_ESTIMATION_PER_MAIN_COMPANY_ID = """SELECT * FROM daily_sales_estimation WHERE main_company_id = {MAIN_COMPANY_ID};"""
            query = CONST_SQL_GET_DAILY_ESTIMATION_PER_MAIN_COMPANY_ID.format(MAIN_COMPANY_ID=str(main_company_id))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            df['estimation'] = df['estimation'].astype((float))
            return df
        finally:
            cur.close()

    def get_main_company_info_details_from_ticker(self, ticker):
        engine = self.get_create_engine()
        query = """SELECT * FROM maincompany WHERE ticker_bbg= '{TICKER}';""".format(TICKER=str(ticker))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get_main_company_info_details_from_ticker_yfinance(self, ticker):
        engine = self.get_create_engine()
        query = """SELECT * FROM maincompany WHERE ticker_yfinance= '{TICKER}';""".format(TICKER=str(ticker))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get_main_company_info_details_from_main_company_id(self, main_company_id):
        engine = self.get_create_engine()
        query = """SELECT * FROM maincompany WHERE id = {MAIN_COMPANY_ID}""".format(MAIN_COMPANY_ID=str(main_company_id))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def insert_reported_sales(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'reported_sales'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_company_table(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['is_parent_company', 'twitter_cashtag', 'google_trend_keyword', 'twitter_url', 'id']]
        try:
            CONST_SQL_UPDATE_COMPANY_TABLE_CASHTAG_PARENT_COMP_GOOGLE_TRENDS = """UPDATE company SET is_parent_company=%s,
            twitter_cashtag=%s, google_trend_keyword=%s, twitter_url=%s WHERE id = %s"""

            cur.executemany(CONST_SQL_UPDATE_COMPANY_TABLE_CASHTAG_PARENT_COMP_GOOGLE_TRENDS, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_company_table_gtrend_url(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['google_trend_url', 'id']]
        try:
            CONST_SQL_UPDATE_COMPANY_GOOGLE_TRENDS_URL = """UPDATE company SET google_trend_url=%s WHERE id = %s"""

            cur.executemany(CONST_SQL_UPDATE_COMPANY_GOOGLE_TRENDS_URL, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_company_name(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['name', 'id']]
        try:
            CONST_SQL_UPDATE_MAIN_COMPANY_TABLE_NAME = 'UPDATE maincompany SET name = %s WHERE id = %s'
            cur.executemany(CONST_SQL_UPDATE_MAIN_COMPANY_TABLE_NAME, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_main_company_table_y_finance(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['ticker_yfinance', 'id']]
        try:
            CONST_SQL_UPDATE_MAIN_COMPANY_TABLE_YFINANCE = 'UPDATE maincompany SET ticker_yfinance = %s WHERE id = %s'

            cur.executemany(CONST_SQL_UPDATE_MAIN_COMPANY_TABLE_YFINANCE, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def update_company_table_twitter_url(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        df = df[['twitter_url', 'id']]
        try:
            CONST_SQL_UPDATE_COMPANY_TABLE_TWIITER_URL = """UPDATE company SET twitter_url=%s WHERE id = %s"""
            cur.executemany(CONST_SQL_UPDATE_COMPANY_TABLE_TWIITER_URL, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_cached_prices(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'historical_prices_cached'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_new_main_comapny(self, df):
        engine = self.get_create_engine()
        table_name = 'maincompany'
        df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')

    def insert_new_comapny(self, df):
        engine = self.get_create_engine()
        table_name = 'company'
        df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')

    def insert_specific_historical_price(self, df):
        engine = self.get_create_engine()
        table_name = 'historical_prices'
        df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')

    def insert_company_detail(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            df = df[['main_company_id', 'market_cap', 'sector', 'sub_sector']]

            INST_SQL_COMPANY_DETAIL = 'INSERT INTO company_detail (main_company_id, market_cap, sector, sub_sector) VALUES(%s, %s, %s, %s)'
            cur.executemany(INST_SQL_COMPANY_DETAIL, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def insert_daily_estimation(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'daily_sales_estimation'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False,  method='multi')
            print('daily revenue estimation inserted correctly into DB')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_old_price(self, timestamp):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            DELETE_SQL_OLD_HISTORICAL_PRICES = """DELETE FROM historical_prices_cached WHERE compute_datetime <= '{TIMESTAMP}'"""
            query = DELETE_SQL_OLD_HISTORICAL_PRICES.format(TIMESTAMP=str(timestamp))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_specific_old_historical_price(self, main_company_id):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            DELETE_OLD_SPECIFIC_HISTORICAL_PRICE = """DELETE FROM historical_prices WHERE main_company_id = {MAIN_COMPANY_ID}"""
            query = DELETE_OLD_SPECIFIC_HISTORICAL_PRICE.format(MAIN_COMPANY_ID=str(main_company_id))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_company_detail(self, df):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            df = df[['main_company_id']]

            DELETE_COMPANY_DETAIL = """DELETE FROM company_detail WHERE main_company_id=%s"""
            cur.executemany(DELETE_COMPANY_DETAIL, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def truncate_historical_price(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            TRUNCATE_HISTORICAL_PRICES_TABLE = 'TRUNCATE TABLE historical_prices RESTART IDENTITY;'
            cur.execute(TRUNCATE_HISTORICAL_PRICES_TABLE)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()


if __name__ == "__main__":
    conn = psql_db_financial_data_gcp()
    df = conn.get_reported_sales_from_main_company_id(main_company_id=1000)
    print(df)
