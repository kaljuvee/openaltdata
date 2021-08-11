import logging
import requests
import json
import sqlalchemy as db
import db.dbutil.news.dbconfig as db_query
import pandas as pd

token = 'oSyQfYcRShExGJmJPXRgr4kOFAsIHqoJ'
#token = 'YFX4ny5glFWKLMGW4EBd9WVckdvGa5QJ'
url = "https://api-eit.refinitiv.com/permid/calais"
DB_URL = 'postgres://altsignals:altdata2$2@35.228.179.179:5432/altsignals-beta'
engine = db.create_engine(DB_URL)
conn = engine.connect()
metadata = db.MetaData()
news_item = db.Table('news_item', metadata, autoload=True, autoload_with=engine)
entity_company = db.Table('entity_company', metadata, autoload=True, autoload_with=engine)
topic = db.Table('topic', metadata, autoload=True, autoload_with=engine)
logging.basicConfig(level=logging.INFO)
trit_request_limit = 1200


def get_news_result():
    get_news_query = db.select([news_item.columns.news_item_id]).where(news_item.columns.language == 'en')
    news_df = pd.read_sql_query(get_news_query, engine)
    return news_df


def get_entity_result():
    entity_id_query = db.select([entity_company.columns.news_item_id])
    entity_df = pd.read_sql_query(entity_id_query, engine)
    return entity_df


def get_result_diff():
    news_df = get_news_result()
    entity_df = get_entity_result()
    new_id_df = pd.concat([news_df, entity_df]).drop_duplicates(keep=False)
    return new_id_df


def get_news_update():
    diff_df = get_result_diff()
    small_df = diff_df.iloc[-trit_request_limit:]
    in_list = small_df['news_item_id'].values.tolist()
    get_update_query = db.select([news_item.columns.news_item_id, news_item.columns.summary],
                                 news_item.columns.news_item_id.in_(in_list))
    news_result = conn.execute(get_update_query)

    return news_result


def extract_entity_trit():
    news_result = get_news_update()
    for r in news_result:
        try:
            JSONResponse = get_trit(r['summary'])
            print('entity_extraction for id:', r['news_item_id'])
            store_entity(r['news_item_id'], JSONResponse)
        except Exception:
            print("Refinitiv api doesn't respond")
            continue


def store_entity(news_id, JSONResponse):
    for entity in JSONResponse:
        for info in JSONResponse[entity]:
            if (info =='resolutions'):
                for companyinfo in (JSONResponse[entity][info]):
                    if 'primaryric' in companyinfo:
                        print('inserting RIC:', companyinfo['primaryric'])
                        ec_ins = entity_company.insert().values(name=companyinfo['name'],
                                                                ric=companyinfo['primaryric'],
                                                                news_item_id=news_id)
                        conn.execute(ec_ins)


def check_entity(ric, news_id):
    exists_query = db.select([entity_company.columns.entity_company_id]).where(entity_company.columns.ric == ric and entity_company.columns.news_item_id == news_id)
    exists = conn.execute(exists_query)
    return exists.scalar() is not None


def get_trit(content):
    headType = "text/raw"
    payload = content.encode('utf8')
    headers = {
        'Content-Type': headType,
        'X-AG-Access-Token': token,
        'outputformat': "application/json"}

    TRITResponse = requests.request("POST", url, data=payload, headers=headers)
    # Load content into JSON object
    try:
        JSONResponse = json.loads(TRITResponse.text)
    except json.decoder.JSONDecodeError as err:
        print("JSON decoding error: ", TRITResponse.text)
        raise err
    return JSONResponse


def main():
    extract_entity_trit()


if __name__ == "__main__":
    main()