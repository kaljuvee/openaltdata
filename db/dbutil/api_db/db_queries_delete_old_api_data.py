import psycopg2
import db.db_access as access

DELETE_SQL_OLD_LIVE_PRICE = """DELETE FROM prices WHERE compute_datetime <= '{TIMESTAMP}' AND period = '{PERIOD}'"""
DELETE_SQL_OLD_PRICE = """DELETE FROM prices WHERE compute_datetime <= '{TIMESTAMP}'"""



class psql_db_altcap_api_connector(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud_altcap_api()

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def delete_old_price(self, timestamp):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = DELETE_SQL_OLD_PRICE.format(TIMESTAMP=str(timestamp))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_old_price_min_hour(self, timestamp, period):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = DELETE_SQL_OLD_LIVE_PRICE.format(TIMESTAMP=str(timestamp), PERIOD=str(period))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def delete_old_data_api_db(self, table_name, timestamp):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            DELETE_SQL_OLD_DATA_API_DB = """DELETE FROM {TABLE_NAME} WHERE compute_datetime <= '{TIMESTAMP}'"""
            query = DELETE_SQL_OLD_DATA_API_DB.format(TABLE_NAME=str(table_name), TIMESTAMP=str(timestamp))
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()

    def vacuum_db(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            CONST_SQL_REFRESH_ALL_TRAFFIC_MAT_VIEW = """VACUUM FULL;"""
            cur.execute(CONST_SQL_REFRESH_ALL_TRAFFIC_MAT_VIEW)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
