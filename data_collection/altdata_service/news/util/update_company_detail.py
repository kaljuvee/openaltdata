from db.dbutil.news.db_queries_news_data import psql_db_news_data_gcp
from data_collection.financial_service.providers.refinitiv.refinitiv_obj import refinitiv
from data_collection.financial_service.providers.EOD.company_details import get_eod_company_detail
from data_collection.financial_service.providers.EOD.EOD_obj import EOD

import pandas as pd


def main():
    # update_entity_table()
    update_news_table()


def update_entity_table():
    data = []

    conn = psql_db_news_data_gcp()
    eod_obj = EOD()

    # get all the exchanges available from EOD, with their MIC info etc
    exchange_detail_list = eod_obj.get_exchange_detail().dropna().reset_index(drop=True)

    # get the table with the entites
    entity_company = conn.get_entity_company().drop_duplicates(subset='ric', keep=False)
    ref_obj = refinitiv()

    t = 1

    for i in entity_company.index:
        entity_company_id = entity_company.at[i, 'entity_company_id']
        ric = entity_company.at[i, 'ric']
        to_slice = ric.find('.')
        ticker = ric[:to_slice]
        ric_exchange_code = ric[to_slice + 1:]

        # get the Market instrument code (exchange code name)
        mic = ref_obj.get_ticker_mic(ric)

        if (mic == 'XNGS') or (ric_exchange_code == 'OQ'):
            country_code = 'US'

        elif mic == None:
            continue

        else:
            try:
                country_code = exchange_detail_list[exchange_detail_list['OperatingMIC'].str.contains(mic)]['Code'].values[0]
            except:
                continue

        # get the ticker for EOD format
        ticker_eod = str(ticker + '.' + country_code)

        # if country code and ticker missing then no point in going furhter
        if (country_code == None) or (ticker_eod == None):
            continue

        # get the market cap sector info from the company
        market_cap, sector, sub_sector = get_eod_company_detail(ticker_eod)

        # append all the data found into the list
        data.append({'entity_company_id': entity_company_id,
                     'market_cap': market_cap,
                     'sector': sector,
                     'sub_sector': sub_sector,
                     'ticker': ticker,
                     'ticker_eod': ticker_eod,
                     'ric': ric})

        # return an indicator how many files we have proceeded during the loop
        if t % 10 == 0:
            print('we have processed ', t, ' files')

        t += 1

    # conver the dictionary into dataframe for later
    df = pd.DataFrame(data)

    # update the table with the new info
    conn.update_entity_company(df)


def update_news_table():
    data = []

    conn = psql_db_news_data_gcp()
    eod_obj = EOD()

    # get all the exchanges available from EOD, with their MIC info etc
    exchange_detail_list = eod_obj.get_exchange_detail().dropna().reset_index(drop=True)

    # get the table with the entites
    entity_company = conn.get_news_table().drop_duplicates(subset='ticker', keep=False).dropna().reset_index(drop=True)
    ref_obj = refinitiv()

    t = 1

    for i in entity_company.index:
        ric = entity_company.at[i, 'ticker']
        to_slice = ric.find('.')
        ticker = ric[:to_slice]
        ric_exchange_code = ric[to_slice + 1:]

        # get the Market instrument code (exchange code name)
        mic = ref_obj.get_ticker_mic(ric)

        if (mic == 'XNGS') or (ric_exchange_code == 'OQ'):
            country_code = 'US'

        elif mic == None:
            continue

        else:
            try:
                country_code = exchange_detail_list[exchange_detail_list['OperatingMIC'].str.contains(mic)]['Code'].values[0]
            except:
                continue

        # get the ticker for EOD format
        ticker_eod = str(ticker + '.' + country_code)

        # if country code and ticker missing then no point in going furhter
        if (country_code == None) or (ticker_eod == None):
            continue

        # get the market cap sector info from the company
        market_cap, sector, sub_sector = get_eod_company_detail(ticker_eod)

        # append all the data found into the list
        data.append({'market_cap': market_cap,
                     'sector': sector,
                     'sub_sector': sub_sector,
                     'ticker_normal': ticker,
                     'ticker_eod': ticker_eod,
                     'ticker': ric})

        # return an indicator how many files we have proceeded during the loop
        if t % 10 == 0:
            print('we have processed ', t, ' files')

        t += 1

    # convert the dictionary into dataframe for later
    df = pd.DataFrame(data)

    # update the table with the new info
    conn.update_new_table(df)


if __name__ == "__main__":
    main()
