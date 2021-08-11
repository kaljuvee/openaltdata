import os.path
import yfinance as yf
import data_collection.altdata_service.nlp.util as util
import data_collection.altdata_service.nlp.dbutil as dbutil
import logging

logging.basicConfig(level=logging.INFO)

def store_fundamentals():
    company = dbutil.entity_company
    ric_query = dbutil.db.select([company.columns.ric.distinct()])
    ric_result = dbutil.conn.execute(ric_query).fetchall()
    try:
        for r in ric_result:
            #logging.info(r['ric'])
            root_symbol = util.get_root_symbol(r['ric'])
            ticker = get_ticker(root_symbol)
    except:
            logging.error('Failed to get fundamentals for:', root_symbol)
    else:
        update = dbutil.update(company).values(market_cap=ticker.info['marketCap'], sector=ticker.info['sector'], ticker=root_symbol)
        update = update.where(company.columns.ric == r['ric'])
        dbutil.conn.execute(update)

def get_ticker(symbol):
    try:
        #logging.info(symbol)
        ticker = yf.Ticker(symbol)
    except Exception:
        logging.error('Exception in get_ticker', symbol)
    return ticker

def main():
    print(os.path)
    store_fundamentals()

if __name__ == "__main__":
    main()