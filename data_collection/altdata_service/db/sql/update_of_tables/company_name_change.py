from db.dbutil.financial_data.db_queries_financial_data import psql_db_financial_data_gcp


def update_company_table_with_google_sheet():
    """
    short script to update the main_company table name, add capital letter on the first letter
    :return:
    """

    conn = psql_db_financial_data_gcp()
    main_company_table = conn.get_main_company()

    for i in main_company_table.index:
        name = main_company_table.at[i, 'name']

        modified_name = name[0].upper() + name[1:]

        main_company_table.at[i, 'name'] = modified_name

    conn.update_company_name(main_company_table)


if __name__ == "__main__":
    print('start of the process')
    update_company_table_with_google_sheet()
    print('process executed correctly')
