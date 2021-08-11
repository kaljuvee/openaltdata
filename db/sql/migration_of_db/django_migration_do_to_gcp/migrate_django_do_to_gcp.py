from db.sql.migration_of_db.django_migration_do_to_gcp.sql_queries import gcp_psql_db_migration
from db.sql.migration_of_db.django_migration_do_to_gcp.sql_queries import do_psql_db_migration
import argparse

gcp_conn = gcp_psql_db_migration()
do_conn = do_psql_db_migration()


def migrate_table(table_name):
    do_table = do_conn.get_table(table_name)
    gcp_table = gcp_conn.get_table(table_name)

    filtered_data = filter_existent_data(gcp_table, do_table)

    if not filtered_data.empty:
        gcp_conn.insert_data(filtered_data, table_name)
    else:
        print('no new data to migrate')

    return


def filter_existent_data(gcp_table, do_table):
    df = do_table[~do_table.iloc[:, 0].isin(gcp_table.iloc[:, 0])]
    return df


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('table_name')
    args = parser.parse_args()
    print(args)
    migrate_table(table_name=args.table_name)
    """
    table_name = 'authtoken_token'
    migrate_table(table_name)

