import sqlalchemy as connector

def get_sqlalchemy_connector():
    DB_URL = 'postgres://altsignals:altdata2$2@35.228.179.179:5432/altsignals-beta'
    engine = connector.create_engine(DB_URL)
    conn = engine.connect()
    db = connector
    metadata = connector.MetaData()
    news_item = connector.Table('news_item', metadata, autoload=True, autoload_with=engine)
    entity_company = connector.Table('entity_company', metadata, autoload=True, autoload_with=engine)
    topic = connector.Table('topic', metadata, autoload=True, autoload_with=engine)
    return connector
