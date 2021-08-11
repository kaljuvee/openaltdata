import sqlalchemy as db
from pandas_datareader import data as pdr
import yfinance as yf
import arrow




# US market opens 8:30AM local / 13:30 GMT and closes 4:00PM local / 9:00pm / 21:00 GMT
#
def get_market_period(published):
     if published.hour < 14:
         market_period = 'BeforeMarket'
     elif published.hour >= 21:
         market_period = 'AfterMarket'
     else:
         market_period = 'MarketHours'
     return market_period

def main():
    store_price_move()

if __name__ == "__main__":
    main()