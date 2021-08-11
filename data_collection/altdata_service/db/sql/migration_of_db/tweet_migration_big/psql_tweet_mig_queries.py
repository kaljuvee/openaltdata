from sqlalchemy import MetaData, Table, create_engine, select
import psycopg2
import pandas as pd
import db.db_access as access

DELETE_QUERY_MIGRATION_TWEET = """DELETE FROM {NAME} WHERE id = %s;"""


class psql_connector_twitter_mig(object):
    def __init__(self):
        self.engine = create_engine('postgres://altcap_usr:M@ch1neTallinn@35.228.179.179:5432/altcap-beta')
        self.metadata = MetaData()
        self.table_name = None
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud_altcap_api()

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_twitter(self, table_name):
        tweet_table = Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
        query = select([tweet_table]).limit(1000)
        tweet_df = pd.DataFrame(data=self.engine.execute(query).fetchall(), columns=self.engine.execute(query).keys()).sort_index()
        return tweet_df

    def delete_imported_tweets(self, df, table_name):
        address_table = Table(table_name, self.metadata, autoload=True, autoload_with=self.engine)
        condition = address_table.c.id.in_(df['id'])
        delete = address_table.delete().where(condition)
        self.engine.execute(delete)

    def delete_imported_tweets_fast(self, df, table_name):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            df = df[['id']]
            query = DELETE_QUERY_MIGRATION_TWEET.format(NAME=str(table_name))
            cur.executemany(query, df.values.tolist())
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
