import db.db_access as access
import model.crunching_data.process as pr
import mysql.connector
import pandas as pd

CONST_USE_FAST = True
CONST_SQL_GET_COMP_NAME = 'SELECT * FROM altdata.company;'
CONST_SQL_GET_COMP_NAMEw = 'SELECT * FROM altdata.company WHERE company_name = "{}";'
CONST_SQL_VIEW_AGG_REPORT_SALES = 'SELECT * FROM altdata.quarter_ends;'
CONST_SQL_GET_COMP_DETAIL = 'SELECT * FROM altdata.company_detail;'
CONST_SQL_GET_AGG_EVERYTHING = 'SELECT * FROM altdata.z_materialised_view_everything;'
CONST_SQL_GET_com_AGG_EVERYTHING = 'SELECT * FROM altdata.z_materialised_view_everythingDotCom;'
CONST_SQL_GET_APP_DETAIL = 'SELECT * FROM altdata.app_detail;'
CONST_SQL_GET_WEB_VISIT = 'SELECT webtraffic.site, webtraffic.datetime, webtraffic.total_visits FROM webtraffic WHERE site like "%.com";'
CONST_SQL_GET_WEB_APP_TRAFFIC = 'SELECT * FROM altdata.aggTraffic_mv;'
CONST_SQL_GET_APP_VISIT = 'SELECT app, datetime, daily_active_users  FROM altdata.apptraffic;'
CONST_SQL_GET_REP_SALES = 'SELECT * FROM altdata.quarter_ends;'
CONST_SQL_GET_REP_SALESw = 'SELECT * FROM altdata.reported_sales LEFT JOIN altdata.company ON altdata.reported_sales.company_id = altdata.company.company_id WHERE company_name = "{}";'
CONST_SQL_GET_HIST_PRICES = 'SELECT historical_prices.company_id, company.ticker, historical_prices.date, historical_prices.close, historical_prices.high, historical_prices.low, historical_prices.open FROM altdata.historical_prices LEFT JOIN altdata.company ON historical_prices.company_id = company.company_id;'
CONST_SQL_UPD_COMP_NUM = "UPDATE `altdata`.`company` SET `companynumber`=? WHERE `idcompany`=?"
CONST_SQL_MINMAX_DATE = 'SELECT Min(datetime), MAX(datetime) FROM alt data.company RIGHT JOIN webtraffic ON company.domain = webtraffic.site WHERE ticker  = {};'
CONST_SQL_SALES_EST = 'SELECT company.company_name, company.ticker, daily_sales_estimation.company_id, daily_sales_estimation.group, daily_sales_estimation.year_estimation, daily_sales_estimation.quarter_estimation, daily_sales_estimation.datetime, daily_sales_estimation.estimation FROM altdata.daily_sales_estimation LEFT JOIN company ON daily_sales_estimation.company_id = company.company_id;'
CONST_SQL_SALES_ESTw = 'SELECT company.company_name, company.ticker, daily_sales_estimation.company_id, daily_sales_estimation.group, daily_sales_estimation.year_estimation, daily_sales_estimation.quarter_estimation, daily_sales_estimation.datetime, daily_sales_estimation.estimation FROM altdata.daily_sales_estimation LEFT JOIN company ON daily_sales_estimation.company_id = company.company_id WHERE company_name = "{}";'
test = 'SELECT company_detail.company_id as company_id, webtraffic.datetime as datetime, sum(webtraffic.total_visits) as total_visits FROM altadata.company_detail INNER JOIN webtraffic ON company_detail.domain = webtraffic.site GROUP BY company_id, datetime;'
CONST_SQL_INSERT_agg3 = "INSERT INTO `altdata`.`tmp_company_id_aggregate3` (`company_id`, `year`, `month`, `total_visits`) VALUES (?, ?, ?, ?)"
CONST_SQL_GET_QUARTER_ENDS = "SELECT * FROM altdata.quarter_ends;"
CONST_SQL_GET_MAX_DATE_WEBTRAFFIC = 'SELECT max(dte) FROM altdata.z_materialised_view_aggTrafficDotCom WH ERE company_id = "{COMPANY_ID}";'
CONST_SQL_GET_com_AGG_EVERYTHING_LONG = 'SELECT * FROM altdata.z_materialised_view_everything_longDotCom;'

CONST_SQL_GET_AGG_ALL = """
SELECT DISTINCT
    s.filing_date,
    s.quarter_group,
    s.sales_reported,
    e.datetime,
    ROUND(e.estimation),
    SUM(w.total_visits)
FROM
    daily_sales_estimation e
        LEFT JOIN
    reported_sales s ON s.company_id = e.company_id
        AND s.quarter_group = e.quarter_group
        LEFT JOIN
    company_detail d ON d.company_id = e.company_id
        LEFT JOIN
    company c ON c.company_id = e.company_id
        LEFT JOIN
    tmp_webtraffic_aggregates2 w ON w.site = d.domain
        AND (w.year + 2000) = e.year_estimation
        AND w.quart = e.quarter_estimation
WHERE
    (e.quarter_group , e.datetime) IN (SELECT 
            e.quarter_group, MAX(e.datetime)
        FROM
            daily_sales_estimation e
        WHERE
            e.company_id = '{}'
                AND e.quarter_group >= '16q3'
                AND e.quarter_group <= '19q4'
        GROUP BY e.quarter_group)
        AND c.ticker = '{}'
GROUP BY c.ticker , c.company_id , s.filing_date , s.quarter_group , s.sales_reported , e.datetime , ROUND(e.estimation)
ORDER BY s.filing_date;
"""

CONST_GET_TRAFFIC_SQL = """select * from tmp_company_id_aggregate2;"""

CONST_GET_TRAFFIC_TEMPLATE = """select * from tmp_company_id_aggregate2 where ticker = '{TICKER}';"""


CONST_GET_SALES_TEMPLATE = """
SELECT 
    reported_sales.company_id, quarter_group, start_quarter_date, end_quarter_date, filing_date, actual_sales, 
    sales_reported, time_announcement, ticker, active 
FROM 
    altdata.reported_sales 
LEFT JOIN altdata.company 
    ON altdata.reported_sales.company_id = altdata.company.company_id
where altdata.reported_sales.company_id = {COMPANY_ID};
 """

CONST_GET_SALES_TEMPLATE_BY_TICKER = """
SELECT 
    reported_sales.company_id, quarter_group, start_quarter_date, end_quarter_date, filing_date, actual_sales, 
    sales_reported, time_announcement, ticker, active 
FROM 
    altdata.reported_sales 
LEFT JOIN altdata.company 
    ON altdata.reported_sales.company_id = altdata.company.company_id
where altdata.reported_sales.company_id = "{TICKER}";
 """


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

    def get_quarterly_sales(self):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(CONST_SQL_GET_REP_SALES)

        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}

        cursor.close()
        cnx.close()
        return result

    def get_companies_names(self):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(CONST_SQL_GET_COMP_NAME)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_quarterly_traffic(self):
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(CONST_GET_TRAFFIC_SQL)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

#TODO get this data from z_materialised_view_agg_traffic, not from a temp table
    def get_quarterly_traffic_for_company(self, ticker):
        sql_request = CONST_GET_TRAFFIC_TEMPLATE.format(TICKER=str(ticker))
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_quarterly_sales_for_company(self, ticker):
        """
        Returns quarterly sales for specific company.
        Among the column names the column "group" actually means quarter
        :param company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        sql_request = CONST_GET_SALES_TEMPLATE_BY_TICKER.format(TICKER=str(ticker))
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

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

    def get_historical_prices(self):
        sql_request = CONST_SQL_GET_HIST_PRICES
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_agg_app_web_traffic(self):
        sql_request = ''
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_agg_everything(self):
        sql_request = CONST_SQL_GET_AGG_EVERYTHING
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_com_agg_everything(self):
        sql_request = CONST_SQL_GET_com_AGG_EVERYTHING
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_com_agg_everything_long(self):
        sql_request = CONST_SQL_GET_com_AGG_EVERYTHING_LONG
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_reported_sales_estimation(self):
        sql_request = CONST_SQL_GET_QUARTER_ENDS
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_max_webtraffic_date_com(self, company_id):
        sql_request = CONST_SQL_GET_MAX_DATE_WEBTRAFFIC.format(COMPANY_ID=str(company_id))
        cnx = self.get_mysql_context()
        cursor = cnx.cursor()
        cursor.execute(sql_request)
        result = {"result": cursor.fetchall(), "header": first_column(cursor.description)}
        cursor.close()
        cnx.close()
        return result

    def get_max_webtraffic_date_com_pandas(self, company_id):
        df = db_result_to_pandas(self.get_max_webtraffic_date_com(company_id))
        return df

    def get_quarterly_sales_pandas(self):
        df = db_result_to_pandas(self.get_quarterly_sales())
        df['time'] = df['time'].map(pr.convert_timedelta_to_time)
        return df

    def get_reported_sales_pandas(self):
        df = db_result_to_pandas(self.get_reported_sales())
        df['time'] = df['time'].map(pr.convert_timedelta_to_time)
        return df

    def get_reported_sales_estimation_pandas(self):
        df = db_result_to_pandas(self.get_reported_sales_estimation())
        df['time'] = df['time'].map(pr.convert_timedelta_to_time)
        return df

    def get_companies_names_pandas(self):
        return db_result_to_pandas(self.get_companies_names())

    def get_quarterly_traffic_company_pandas(self, ticker):
        return db_result_to_pandas(self.get_quarterly_traffic_for_company(ticker))

    def get_quarterly_sales_for_company_pandas(self, ticker):
        """
        Returns quarterly sales for specific company.
        Among the column names the column "group" actually means quarter
        :param company_id:
        :return: {"result": <query result>, "header": <names of the columns>
        """
        return db_result_to_pandas(self.get_quarterly_sales_for_company(ticker))

    def get_historical_prices_pandas(self):
        return db_result_to_pandas(self.get_historical_prices())

    def get_agg_app_web_traffic_pandas(self):
        return db_result_to_pandas(self.get_agg_app_web_traffic())

    def get_agg_everything_pandas(self):
        df = db_result_to_pandas(self.get_agg_everything())
        df['time'] = df['time'].map(pr.convert_timedelta_to_time)
        return df

    def get_agg_everything_pandas_2(self):
        df = db_result_to_pandas(self.get_agg_everything())
        df['time'] = df['time_announcement'].map(pr.convert_timedelta_to_time)
        return df

    def get_com_agg_everything_pandas(self):
        df = db_result_to_pandas(self.get_com_agg_everything())
        df['time_announcement'] = df['time_announcement'].map(pr.convert_timedelta_to_time)
        return df

    def get_com_agg_everything_long_pandas(self):
        df = db_result_to_pandas(self.get_com_agg_everything_long())
        df['time_announcement'] = df['time_announcement'].map(pr.convert_timedelta_to_time)
        return df

    def get_signal_chart_csv(self, ticker):
        df = pd.read_csv(r'https://docs.google.com/spreadsheets/d/e/2PACX-1vTSW8rjszK3jUfReRqUnpoFOPtSFVVWn6AFJGBkowxUvs57zpkxCIG64Xwj89U2v0x9Ye1vO1SgKbQD/pub?gid=1496289040&single=true&output=csv')
        df = df[df.ticker == ticker + " US"]
        df = df[['ticker', 'end_quarter_date', 'Actual', 'Estimation', 'AltSignals']]
        return df

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

