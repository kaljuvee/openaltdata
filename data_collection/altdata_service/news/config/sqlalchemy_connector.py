import sqlalchemy as connector

DB_URL = 'postgresql://altsignals:altdata2$2@35.228.179.179:5432/altsignals-beta'
engine = connector.create_engine(DB_URL)
conn = engine.connect()
db = connector
metadata = connector.MetaData()

