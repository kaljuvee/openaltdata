import sqlalchemy as connector

DB_URL = 'postgres://altcap_usr:M@ch1neTallinn@35.228.179.179:5432/altcap-beta'
engine = connector.create_engine(DB_URL)
conn = engine.connect()
metadata = connector.MetaData()
day_keyword_materialised = connector.Table('day_keyword_materialised', metadata, autoload=True, autoload_with=engine)