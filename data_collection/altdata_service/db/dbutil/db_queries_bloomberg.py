import db.db_access as access
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


CONST_SQL_GET_COMP_NAME = 'SELECT * FROM maincompany;'
CONST_SQL_GET_REP_SALES = 'SELECT * FROM reported_sales;'
CONST_SQL_GET_DAILY_ESTIMATION = 'SELECT * FROM daily_sales_estimation;'
CONST_SQL_GET_DAILY_ESTIMATION_PER_MAIN_COMPANY_ID = 'SELECT * FROM daily_sales_estimation WHERE main_company_id = {MAIN_COMPANY_ID};'
CONST_SQL_GET_HIST_PRICES = 'SELECT * FROM historical_prices;'

INSERT_REPORTED_SALES = 'INSERT INTO reported_sales (main_company_id, quarter_group, end_quarter_date, start_quarter_date, filing_date, actual_sales, sales_reported, time_announcement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
INSERT_DAILY_SALES_ESTIMATION = 'INSERT INTO daily_sales_estimation (main_company_id, quarter_group, year_estimation, quarter_estimation, datetime, estimation) VALUES (%s, %s, %s, %s, %s, %s)'
INSERT_HIST_PRICE = 'INSERT INTO historical_prices (main_company_id, date, close, high, low, open) VALUES (%s, %s, %s, %s, %s, %s)'

DELETE_DAILY_ESTIMATION_FUTURE = 'DELETE FROM daily_sales_estimation WHERE company_id = %s and quarter_group = %s;'


def first_column(array_2d):
    return list(zip(*array_2d))[0]


def db_result_to_pandas(cursor_fetch_result):
    return pd.DataFrame(cursor_fetch_result['result'], columns=cursor_fetch_result['header'])


class psql_bloomberg_pipeline_connector_db(object):
    """
    Class for getting data from the database.
    Currently not SQL injection safe.
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

    def get_companies_names(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_COMP_NAME)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_reported_sales(self):
        """
        Returns reported sales for all companies.
        Among the column names the column "group" actually means quarter
        :param company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_REP_SALES)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

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
            query = CONST_SQL_GET_DAILY_ESTIMATION_PER_MAIN_COMPANY_ID.format(MAIN_COMPANY_ID=str(main_company_id))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_historical_prices(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            cur.execute(CONST_SQL_GET_HIST_PRICES)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def insert_reported_sales(self, df):
        cnx = self.get_psql_context()
        cursor = cnx.cursor()
        try:
            df = df[['main_company_id', 'group', 'end_quarter_date', 'start_quarter_date', 'filing_date', 'actual_sales', 'sales_reported', 'time']]

            # change format for date and time to insert it in db
            df['end_quarter_date'] = df['end_quarter_date'].map(lambda x: x.strftime('%Y-%m-%d'), list(df['end_quarter_date']))
            df['start_quarter_date'] = df['start_quarter_date'].map(lambda x: x.strftime('%Y-%m-%d'), list(df['start_quarter_date']))
            df['filing_date'] = df['filing_date'].map(lambda x: x.strftime('%Y-%m-%d'), list(df['filing_date']))

            cursor.executemany(INSERT_REPORTED_SALES, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()
            cnx.close()

    def insert_daily_estimation(self, df):
        engine = self.get_create_engine()
        try:
            table_name = 'daily_sales_estimation'
            df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_historical_price(self, df):
        cnx = self.get_psql_context()
        cursor = cnx.cursor()
        try:
            df = df[['main_company_id', 'date', 'close', 'high', 'low', 'open']]

            cursor.executemany(INSERT_HIST_PRICE, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()
            cnx.close()

    def delete_daily_estimation_quarter(self, df):
        cnx = self.get_psql_context()
        cursor = cnx.cursor()
        try:
            df = df[['main_company_id', 'quarter_group']]

            cursor.executemany(DELETE_DAILY_ESTIMATION_FUTURE, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()
            cnx.close()


'''
class TrafficDatabaseConnector(object):
    """
    Class for getting data from the database.
    Currently not SQL injection safe.
    """
    def __init__(self):
        server, database, username, password, driver = access.parameter()

        self.cnx = mysql.connector.connect(user=username, password=password,
                                           host=server,
                                           database=database)

    def get_mysql_context(self):
        server, database, username, password, driver = access.parameter()

        cnx = mysql.connector.connect(user=username, password=password,
                                           host=server,
                                           database=database)
        return cnx

    def get_companies_names(self):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(CONST_SQL_GET_COMP_NAME)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_companies_names_pandas(self):
        return db_result_to_pandas(self.get_companies_names())

    def get_reported_sales(self):
        """
        Returns reported sales for all companies.
        Among the column names the column "group" actually means quarter
        :param company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        sql_request = CONST_SQL_GET_REP_SALES
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_reported_sales_pandas(self):
        return db_result_to_pandas(self.get_reported_sales())

    def get_daily_sales_estimation(self):
        """
        Returns reported sales for all companies.
        Among the column names the column "group" actually means quarter
        :param company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        sql_request = CONST_SQL_GET_DAILY_ESTIMATION
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_daily_sales_estimation_pandas(self):
        return db_result_to_pandas(self.get_daily_sales_estimation())

    def get_historical_prices(self):
        sql_request = CONST_SQL_GET_HIST_PRICES
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_historical_prices_pandas(self):
        return db_result_to_pandas(self.get_historical_prices())

    def insert_reported_sales(self, df):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        try:
            df = df[['company_id', 'group', 'end_quarter_date', 'start_quarter_date', 'filing_date', 'actual_sales', 'sales_reported', 'time']]

            # change format for date and time to insert it in db
            df['end_quarter_date'] = df['end_quarter_date'].map(lambda x: x.strftime('%Y-%m-%d'), list(df['end_quarter_date']))
            df['start_quarter_date'] = df['start_quarter_date'].map(lambda x: x.strftime('%Y-%m-%d'), list(df['start_quarter_date']))
            df['filing_date'] = df['filing_date'].map(lambda x: x.strftime('%Y-%m-%d'), list(df['filing_date']))

            cursor.executemany(INSERT_REPORTED_SALES, df.values.tolist())
            cnx.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        finally:
            cursor.close()
            cnx.close()

    def insert_daily_estimation(self, df):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        try:
            df = df[['company_id', 'quarter_group', 'year_estimation', 'quarter_estimation', 'datetime', 'estimation']]

            cursor.executemany(INSERT_DAILY_SALES_ESTIMATION, df.values.tolist())
            cnx.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        finally:
            cursor.close()
            cnx.close()

    def insert_historical_price(self, df):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        try:
            df = df[['company_id', 'date', 'close', 'high', 'low', 'open']]

            cursor.executemany(INSERT_HIST_PRICE, df.values.tolist())
            cnx.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        finally:
            cursor.close()
            cnx.close()

    def delete_daily_estimation_quarter(self, df):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        try:
            df = df[['company_id', 'quarter_group']]

            cursor.executemany(DELETE_DAILY_ESTIMATION_FUTURE, df.values.tolist())
            cnx.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
        finally:
            cursor.close()
            cnx.close()


    def _run_sql_query(self, sql_request):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def run_sql_query(self, sql_request):
        return db_result_to_pandas(self._run_sql_query(sql_request))


def cache_db_request_pandas(db_request, pandas_filename):
    try:
        return pd.read_pickle(pandas_filename)
    except Exception as e:
        pandas_obj = db_request()
        pandas_obj.to_pickle(pandas_filename)
        return pandas_obj
'''
