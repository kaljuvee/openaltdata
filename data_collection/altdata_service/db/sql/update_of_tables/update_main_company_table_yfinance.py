from config.google_drive_connection.google_spreadsheet import get_gspread_client
import pandas as pd
from db.dbutil.financial_data.db_queries_financial_data import psql_db_financial_data_gcp


def update_yfinance_column_in_main_company_table():
    """
    short script to update the company table missing data for is_parent_company, google trends keyword and twitter_cashtag
    more data can be added in the future if needed
    :return:
    """

    conn = psql_db_financial_data_gcp()

    main_company_table = conn.get_main_company()

    for i in main_company_table.index:
        active = main_company_table.at[i, 'active']

        if not active == True:
            continue

        main_company_id = main_company_table.at[i, 'id']

        ticker_bbg = main_company_table[main_company_table['id'] == main_company_id]['ticker_bbg'].values[0]

        # get the exchange code from bloomberg ticker
        bbg_exchange = ticker_bbg[(ticker_bbg.find(' ')) + 1 :]

        exchange_letter_code = get_exchange_letter_y_finance(bbg_exchange)

        if exchange_letter_code is None:
            main_company_table.at[i, 'ticker_yfinance'] = main_company_table.at[i, 'ticker']
        else:
            main_company_table.at[i, 'ticker_yfinance'] = main_company_table.at[i, 'ticker'] + '.' + exchange_letter_code

    conn.update_main_company_table_y_finance(df=main_company_table[['id', 'ticker_yfinance']])


def get_exchange_letter_y_finance(bbg_exchange):
    if bbg_exchange == 'US':
        return None
    elif bbg_exchange == 'LN':
        return 'L'
    elif bbg_exchange == 'GR':
        return 'DE'
    elif bbg_exchange == 'AU':
        return 'AX'
    elif bbg_exchange == 'SS':
        return 'ST'
    elif bbg_exchange == 'CN':
        return 'TO'
    else:
     return None


if __name__ == "__main__":
    update_yfinance_column_in_main_company_table()
