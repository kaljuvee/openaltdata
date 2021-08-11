import logging
import requests
import json
import sqlalchemy as db

token = 'oSyQfYcRShExGJmJPXRgr4kOFAsIHqoJ'
url = "https://api-eit.refinitiv.com/permid/calais"
DB_URL = 'postgres://altsignals:altdata2$2@35.228.179.179:5432/altsignals-beta'
engine = db.create_engine(DB_URL)
conn = engine.connect()
metadata = db.MetaData()
news_item = db.Table('news_item', metadata, autoload=True, autoload_with=engine)
entity_company = db.Table('entity_company', metadata, autoload=True, autoload_with=engine)
topic = db.Table('topic', metadata, autoload=True, autoload_with=engine)
logging.basicConfig(level=logging.INFO)

def extract_topic():
    get_news_query = db.select([news_item.columns.news_item_id, news_item.columns.summary]).where(news_item.columns.language == 'en')
    news_result = conn.execute(get_news_query).fetchall()
    for r in news_result:
        try:
            JSONResponse = get_trit(r['summary'])
        except:
            print('failed to call TRIT for:', r['summary'])
        else:
            store_topic(r['news_item_id'], JSONResponse)



def store_topic(news_id, JSONResponse):
    print('news_id: ', news_id)
    for key in JSONResponse:
        if ('_typeGroup' in JSONResponse[key]):
            if JSONResponse[key]['_typeGroup'] == 'topics':
                try:
                    if (check_topic(news_id) is not True):
                        print(JSONResponse[key]['name'] + ", " + str(JSONResponse[key]['score']))
                        topic_ins = topic.insert().values(name = JSONResponse[key]['name'],
                                                       score = JSONResponse[key]['score'],
                                                       news_item_id = news_id)
                        conn.execute(topic_ins)
                except:
                    print('Exception in store_topic: ', JSONResponse[key]['_typeGroup'] )

def check_topic(news_id):
    exists_query = db.select([topic.columns.topic_id]).where(topic.columns.news_item_id == news_id)
    exists = conn.execute(exists_query)
    return exists.scalar() is not None

# news_id:  1067
def get_trit(content):
    headType = "text/raw"
    payload = content.encode('utf8')
    headers = {
        'Content-Type': headType,
        'X-AG-Access-Token': token,
        'outputformat': "application/json"
    }
    try:
        TRITResponse = requests.request("POST", url, data=payload, headers=headers)
        # Load content into JSON object
        JSONResponse = json.loads(TRITResponse.text)
    except:
        print('Exception in get_trit: ', content)
    return JSONResponse

def main():
    extract_topic()

if __name__ == "__main__":
    main()