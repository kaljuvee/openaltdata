import sqlalchemy as db

DB_URL = 'postgres://altsignals:altdata2$2@35.228.179.179:5432/altsignals-beta'
engine = db.create_engine(DB_URL)
conn = engine.connect()
metadata = db.MetaData()
news_item = db.Table('news_item', metadata, autoload=True, autoload_with=engine)
entity_company = db.Table('entity_company', metadata, autoload=True, autoload_with=engine)
topic = db.Table('topic', metadata, autoload=True, autoload_with=engine)

