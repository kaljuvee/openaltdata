import pandas as pd
import db.db_access as access
from sqlalchemy import create_engine


class gcp_psql_db_migration(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_table(self, table_name):
        engine = self.get_create_engine()

        query = """SELECT * FROM {TABLE_NAME}"""

        query = query.format(TABLE_NAME=str(table_name))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get__main_company_table(self):
        engine = self.get_create_engine()

        query = """SELECT * FROM maincompany"""

        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get_company_table(self):
        engine = self.get_create_engine()

        query = """SELECT * FROM company"""

        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def insert_data(self, df, table_name):
        engine = self.get_create_engine()
        df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False, method='multi')
        return


class do_psql_db_migration(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_digital_ocean()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_table(self, table_name):
        engine = self.get_create_engine()

        query = """SELECT * FROM {TABLE_NAME}"""

        query = query.format(TABLE_NAME=str(table_name))
        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get__main_company_table(self):
        engine = self.get_create_engine()

        query = """SELECT * FROM maincompany"""

        df = pd.read_sql_query(query, con=engine.connect())
        return df

    def get_company_table(self):
        engine = self.get_create_engine()

        query = """SELECT * FROM company"""

        df = pd.read_sql_query(query, con=engine.connect())
        return df

    """
    def insert_data(self, df, table_name):
        engine = self.get_create_engine()
        df.to_sql(table_name, con=engine.connect(), if_exists='append', index=False)
        return
    """