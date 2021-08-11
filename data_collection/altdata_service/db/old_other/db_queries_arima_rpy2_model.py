from db.dbutil.webtraffic.db_queries_webtraffic_sales import TrafficDatabaseConnector


def get_tickers_with_known_sales_formatted():
    conn = TrafficDatabaseConnector()
    TICKERS_WITH_REPORTED_SALES_KNOWN = """
    SELECT 
        distinct(ticker)
    FROM 
        altdata.company;
    """
    tickers_pandas = conn.run_sql_query(TICKERS_WITH_REPORTED_SALES_KNOWN)
    return list(map(lambda x: x.replace(' ', '.'), set(list(tickers_pandas.ticker))))


def get_ticker_to_company_name_map():
    conn = TrafficDatabaseConnector()
    TICKERS_WITH_REPORTED_SALES_KNOWN = """
    SELECT 
        ticker, company_name
    FROM 
        altdata.company;
    """
    tickers_pandas = conn.run_sql_query(TICKERS_WITH_REPORTED_SALES_KNOWN)
    tickers_pandas.rename(columns={'ticker': 'code'}, inplace=True)
    tickers_pandas['code'] = tickers_pandas.code.map(lambda x: x.replace(' ', '.'))
    return tickers_pandas

