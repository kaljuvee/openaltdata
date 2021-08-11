import pyodbc
from backtesting.internal.web_traffic_sales import webtraffic_sales_model as access

CONST_USE_FAST = True
CONST_SQL_GET_COMP_NAME = 'SELECT * FROM altdata.company;'
CONST_SQL_GET_COMP_NAMEw = 'SELECT * FROM altdata.company WHERE company_name = "{}";'
CONST_SQL_VIEW_AGG_REPORT_SALES = 'SELECT * FROM altdata.quarter_ends;'
CONST_SQL_GET_COMP_DETAIL = 'SELECT * FROM altdata.company_detail;'
CONST_SQL_GET_WEB_VISIT2 = 'SELECT webtraffic.site, webtraffic.datetime, webtraffic.total_visits FROM webtraffic WHERE site like "%.com";'
CONST_SQL_GET_REP_SALES = 'SELECT * FROM altdata.reported_sales LEFT JOIN altdata.company ON altdata.reported_sales.company_id = altdata.company.company_id;'
CONST_SQL_GET_REP_SALESw = 'SELECT * FROM altdata.reported_sales LEFT JOIN altdata.company ON altdata.reported_sales.company_id = altdata.company.company_id WHERE company_name = "{}";'
CONST_SQL_GET_HIST_PRICES = 'SELECT historical_prices.company_id, company.ticker, historical_prices.date, historical_prices.close, historical_prices.high, historical_prices.low, historical_prices.open FROM altdata.historical_prices LEFT JOIN altdata.company ON historical_prices.company_id = company.company_id;'
CONST_SQL_AGG_WEBTRAFFIC = 'SELECT * FROM altdata.tmp_company_id_aggregate2'
CONST_SQL_UPD_COMP_NUM = "UPDATE `altdata`.`company` SET `companynumber`=? WHERE `idcompany`=?"
CONST_SQL_MINMAX_DATE = 'SELECT Min(datetime), MAX(datetime) FROM altdata.company RIGHT JOIN webtraffic ON company.domain = webtraffic.site WHERE ticker  = {};'
CONST_SQL_SALES_EST = 'SELECT company.company_name, company.ticker, daily_sales_estimation.company_id, daily_sales_estimation.group, daily_sales_estimation.year_estimation, daily_sales_estimation.quarter_estimation, daily_sales_estimation.datetime, daily_sales_estimation.estimation FROM altdata.daily_sales_estimation LEFT JOIN company ON daily_sales_estimation.company_id = company.company_id;'
CONST_SQL_SALES_ESTw = 'SELECT company.company_name, company.ticker, daily_sales_estimation.company_id, daily_sales_estimation.group, daily_sales_estimation.year_estimation, daily_sales_estimation.quarter_estimation, daily_sales_estimation.datetime, daily_sales_estimation.estimation FROM altdata.daily_sales_estimation LEFT JOIN company ON daily_sales_estimation.company_id = company.company_id WHERE company_name = "{}";'
test = 'SELECT company_detail.company_id as company_id, webtraffic.datetime as datetime, sum(webtraffic.total_visits) as total_visits FROM altadata.company_detail INNER JOIN webtraffic ON company_detail.domain = webtraffic.site GROUP BY company_id, datetime;'
CONST_SQL_INSERT_agg3 = "INSERT INTO `altdata`.`tmp_company_id_aggregate3` (`company_id`, `year`, `month`, `total_visits`) VALUES (?, ?, ?, ?)"

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
        quarter_group BY e.quarter_group)
        AND c.ticker = '{}'
quarter_group BY c.ticker , c.company_id , s.filing_date , s.quarter_group , s.sales_reported , e.datetime , ROUND(e.estimation)
ORDER BY s.filing_date;
"""

# get the companies details
def getcompanyname(pd, company_name = 'all'):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_GET_COMP_NAME
        if company_name != 'all':
            query = CONST_SQL_GET_COMP_NAMEw.format(company_name)
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()

def get_companyname_detail(pd):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_GET_COMP_DETAIL
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()

def get_view_agg_reported_sales(pd):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_VIEW_AGG_REPORT_SALES
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()


def getminmaxdate(ticker, pd):

    server, database, username, password, driver = access.parameter()

    CONST_SQL_MINMAX_DATE = 'SELECT Min(datetime), MAX(datetime) FROM company RIGHT JOIN webtraffic ON company.domain = webtraffic.site WHERE ticker  = "{}";'.format(ticker)
    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        return pd.read_sql(CONST_SQL_MINMAX_DATE, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()


# get the quaterly total visits on the website
def getwebtrafficvisits(pd):
    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        return pd.read_sql(CONST_SQL_GET_WEB_VISIT2, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()


# get the companies daily sales estimation from the consensus analyst
def getsalesestimation(pd, company_name = 'all'):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_SALES_EST
        if company_name != 'all':
            query = CONST_SQL_SALES_ESTw.format(company_name)
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()

def getreportdsales(pd, company_name = 'all'):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_GET_REP_SALES
        if company_name != 'all':
            query = CONST_SQL_GET_REP_SALESw.format(company_name)
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()

def getaggwebtraffic(pd):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_AGG_WEBTRAFFIC
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()

def get_historical_prices(pd):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        query = CONST_SQL_GET_HIST_PRICES
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()



def update_companynumber(df):
    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        cursor = cnxn.cursor()
        cursor.fast_executemany = CONST_USE_FAST

        df1 = df[['companynumber', 'idcompany']].copy()

        cursor.executemany(CONST_SQL_UPD_COMP_NUM, df1.values.tolist())

        cnxn.commit()

    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cursor.close()
        cnxn.close()


def insert_agg3(df):
    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')
        cursor = cnxn.cursor()
        cursor.fast_executemany = CONST_USE_FAST

        cursor.executemany(CONST_SQL_INSERT_agg3, df.values.tolist())

        cnxn.commit()

    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cursor.close()
        cnxn.close()


# get the companies details
def get_all_agg(pd, ticker, company_id):

    server, database, username, password, driver = access.parameter()

    global cnxn

    try:
        cnxn = pyodbc.connect('DRIVER= ' + driver + ';SERVER= ' + server + ';DATABASE= ' + database + ';USER= ' + username + ' ;PASSWORD= ' + password + ';OPTION=3;')

        query = CONST_SQL_GET_AGG_ALL.format(company_id, ticker)
        return pd.read_sql(query, cnxn, index_col=None)
    except pyodbc.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)
    finally:
        cnxn.close()
