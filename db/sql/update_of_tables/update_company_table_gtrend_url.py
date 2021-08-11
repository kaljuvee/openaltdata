import pandas as pd
from db.dbutil.financial_data.db_queries_financial_data import psql_db_financial_data_gcp


def update_company_table_with_google_sheet():
    """
    short script to update the company table missing data for is_parent_company, google trends keyword and twitter_cashtag
    more data can be added in the future if needed
    :return:
    """

    conn = psql_db_financial_data_gcp()

    df = pd.read_excel('google_trend_url.xlsx')[['id', 'google_trend_url']].dropna()

    df['google_trend_url'] = df['google_trend_url'].replace('%2f', '/')

    conn.update_company_table_gtrend_url(df)


if __name__ == "__main__":
    print('start of the process')
    update_company_table_with_google_sheet()
    print('process executed correctly')
