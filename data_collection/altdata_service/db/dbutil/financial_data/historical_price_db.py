import db.dbutil.financial_data.db_queries_financial_data as db
import pandas as pd


def get_historical_all(main_company_table):
    df = pd.DataFrame()
    db_obj = db.psql_db_financial_data_gcp()

    for i in main_company_table.index:

        ticker_normal = main_company_table.at[i, 'ticker']
        ticker_bbg = main_company_table.at[i, 'ticker_bbg']
        main_company_id = main_company_table.at[i, 'id']

        data = db_obj.get_historical_price_from_ticker(ticker=ticker_normal)

        if data.empty:
            continue

        data['ticker'] = ticker_bbg
        data['main_company_id'] = main_company_id

        df = df.append(data, ignore_index=True)

    return df.reset_index(drop=True)
