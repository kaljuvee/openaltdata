import psycopg2
import db.db_access as access


class GCPostgresConnector(object):
    def __init__(self):
       self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()

    def run_query(self,query):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        cur = cnx.cursor()
        cur.execute(query)
        return {'table': cur.fetchall(), 'colnames':[desc[0] for desc in cur.description]}

    def run_query_row_json(self,query):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        cur = cnx.cursor()
        cur.execute(query)
        colnames = [desc[0] for desc in cur.description]
        table = cur.fetchall()
        row_oriented_table = []
        for elem in table:
            row_dict = {}
            for key, value in zip(colnames, elem):
                row_dict[key] = value
            row_oriented_table.append(row_dict)
        return row_oriented_table


