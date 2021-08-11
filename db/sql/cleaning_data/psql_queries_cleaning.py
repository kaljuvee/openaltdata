import psycopg2
import pandas as pd
import db.db_access as access
from sqlalchemy import create_engine


CONST_SQL_GET_MAIN_COMPANY = 'SELECT * FROM maincompany'
CONST_SQL_GET_COMPANY = 'SELECT * FROM company'
C = """ SELECT "company"."id", "company"."name", "company"."main_company_id", "company"."parent_company_id", "company"."is_parent_company", "company"."indeed_url", "company"."static_indeed_url", "company"."twitter_url", "company"."twitter_cashtag", "company"."twitter_keyword", "company"."google_trend_keyword", "company"."instagram_url", "company"."facebook_url", "company"."linkedin_url", "company"."domain", "company"."date_updated", "company"."webtraffic_hist" FROM "company" WHERE UPPER("company"."domain"::text) LIKE UPPER(%switch.ch%)"""


class DbCleaningCompanyURLWrong(object):
    def __init__(self):
        self.host, self.port, self.database, self.user, self.password = access.postgre_access_google_cloud()
        self.message = str('postgres://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.database)

    def get_psql_context(self):
        cnx = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)
        return cnx

    def get_create_engine(self):
        engine = create_engine(self.message)
        return engine

    def get_main_company(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = 'SELECT * FROM maincompany'
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_company_table(self):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = 'SELECT * FROM company'
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()

    def get_similar_domain_name(self, domain):
        cnx = self.get_psql_context()
        cur = cnx.cursor()
        try:
            query = """ SELECT "company"."id", "company"."name", "company"."main_company_id", "company"."parent_company_id",
             "company"."is_parent_company", "company"."indeed_url", "company"."static_indeed_url", "company"."twitter_url",
              "company"."twitter_cashtag", "company"."twitter_keyword", "company"."google_trend_keyword", "company"."instagram_url",
               "company"."facebook_url", "company"."linkedin_url", "company"."domain", "company"."date_updated", 
               "company"."webtraffic_hist" FROM "company" WHERE UPPER("company"."domain"::text) LIKE UPPER('%{DOMAIN}%')"""
            query = query.format(DOMAIN=str(domain))
            cur.execute(query)
            result = cur.fetchall()
            df = pd.DataFrame.from_records(result, columns=[x[0] for x in cur.description])
            return df
        finally:
            cur.close()
