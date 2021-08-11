import db.db_access as access

import psycopg2


class OtherDBQueries(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def delete_traffic_duplicate(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = """DELETE from traffic WHERE id in (select min_id from (select company_id, date, min(id) as min_id, 
            count(1) as cnt from traffic group by company_id, date) tbl where cnt > 1)"""
            cur.execute(query)
            cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
