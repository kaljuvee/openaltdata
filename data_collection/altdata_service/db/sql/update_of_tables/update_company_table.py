from config.google_drive_connection.google_spreadsheet import get_gspread_client
import pandas as pd
from db.dbutil.financial_data.db_queries_financial_data import psql_db_financial_data_gcp


def update_company_table_with_google_sheet():
    """
    short script to update the company table missing data for is_parent_company, google trends keyword and twitter_cashtag
    more data can be added in the future if needed
    :return:
    """

    conn = psql_db_financial_data_gcp()

    main_company_table = conn.get_main_company()

    # get google spreadsheet client connector
    client = get_gspread_client()
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("update_company_table_data").sheet1
    # Extract and print all of the values
    df = pd.DataFrame(sheet.get_all_records())

    for i in df.index:
        main_company_id = df.at[i, 'main_company_id']
        active = main_company_table[main_company_table['id'] == main_company_id]['active'].values[0]

        if not active == True:
            continue

        ticker = main_company_table[main_company_table['id'] == main_company_id]['ticker'].values[0]

        df.at[i, 'twitter_cashtag'] = str('$' + ticker)

    conn.update_company_table(df)


if __name__ == "__main__":
    print('start of the process')
    update_company_table_with_google_sheet()
    print('process executed corretly')
