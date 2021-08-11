import db.db_access as access
from backtesting.internal import web_traffic_sales as pr
import mysql.connector
import pandas as pd

CONST_SQL_GET_COMP_NAME = 'SELECT * FROM altdata.company;'
CONST_SQL_GET_HIST_PRICES = 'SELECT historical_prices.company_id, company.ticker, historical_prices.date, historical_prices.close, historical_prices.high, historical_prices.low, historical_prices.open FROM altdata.historical_prices LEFT JOIN altdata.company ON historical_prices.company_id = company.company_id;'
CONST_SQL_GET_REP_SALES = 'SELECT * FROM altdata.reported_sales;'
CONS_SQL_AGG_DAILY_TRAFFIC_DOT_COM = 'SELECT * FROM altdata.z_materialised_view_aggTrafficDotCom;'
CONS_SQL_GET_EST = 'SELECT * FROM daily_sales_estimation;'

def first_column(array_2d):
    return list(zip(*array_2d))[0]


def db_result_to_pandas(cursor_fetch_result):
    return pd.DataFrame(cursor_fetch_result['result'], columns=cursor_fetch_result['header'])


class TrafficDatabaseConnector(object):
    """
    Class for getting data from the database.
    Currently not SQL injection safe.
    TODO: make it safe from SQL injections
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
        df = db_result_to_pandas(self.get_reported_sales())
        df['time'] = df['time'].map(pr.convert_timedelta_to_time)
        return df

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

    def get_daily_similar_web_agg_dot_com(self):
        sql_request = CONS_SQL_AGG_DAILY_TRAFFIC_DOT_COM
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_daily_similar_web_agg_dot_com_pandas(self):
        return db_result_to_pandas(self.get_daily_similar_web_agg_dot_com())

    def get_estimation(self):
        sql_request = CONS_SQL_GET_EST
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_estimation_pandas(self):
        return db_result_to_pandas(self.get_estimation())


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