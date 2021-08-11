from db.sql.migration_of_db.django_migration_do_to_gcp.sql_queries import gcp_psql_db_migration
from db.sql.migration_of_db.django_migration_do_to_gcp.sql_queries import do_psql_db_migration
import argparse

gcp_conn = gcp_psql_db_migration()
do_conn = do_psql_db_migration()


def migrate_table(table_name):
    do_table = do_conn.get_table(table_name)

    gcp_company_table = gcp_conn.get_company_table()
    do_company_table = do_conn.get_company_table()

    new_converted_id = convert_company_id_in_gcp(do_table, gcp_company_table, do_company_table)

    if not new_converted_id.empty:
        gcp_conn.insert_data(new_converted_id, table_name)
    else:
        print('no new data to migrate')

    return


def convert_company_id_in_gcp(do_table, gcp_company_table, do_company_table):
    gcp_company_table = gcp_company_table.rename(columns={'id': 'company_id'})
    do_company_table = do_company_table.rename(columns={'id': 'company_id'})

    modified_do_table = do_table.merge(do_company_table[['company_id', 'domain']], on='company_id')
    modified_do_table = modified_do_table.merge(gcp_company_table[['company_id', 'domain']], on='domain')
    modified_do_table = modified_do_table.drop(columns=['company_id_x', 'domain'])
    modified_do_table = modified_do_table.rename(columns={'company_id_y': 'company_id'})
    return modified_do_table.drop_duplicates(subset=['id'])


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('table_name')
    args = parser.parse_args()
    print(args)
    migrate_table(table_name=args.table_name)
    """
    table_name = 'traffic'
    migrate_table(table_name)


