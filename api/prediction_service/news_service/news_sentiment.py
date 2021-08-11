import pandas as pd
import numpy

from db.dbutil.news.dbconfig import NewsConnectorDb


source = 'db'
db = NewsConnectorDb()


def get_news_sentiment_best():
    if source == 'csv':
        sub_df = pd.read_csv('../../../data/news/test_data/news_sentiment_best.csv')
    else:
        df = db.get_news_sentiment_best()
        sub_df = df[0:10]
        sub_df.sort_values(by=['signal'], inplace=True, ascending=False)
    return sub_df


def get_news_sentiment_worst():
    if source == 'csv':
        sub_df = pd.read_csv('../../../data/news/test_data/news_sentiment_worst.csv')
    else:
        df = db.get_news_sentiment_worst()
        sub_df = df[0:10]
        sub_df.sort_values(by=['signal'], inplace=True, ascending=True)
    return sub_df


def get_news_sentiment_map():
    if source == 'csv':
        df = pd.read_csv('../../../data/news/test_data/news_sentiment_map.csv')
    else:
        df = db.get_news_sentiment_map()
        df = fill_size_sentiment_map(df)
    return df


def fill_size_sentiment_map(df):
    size = numpy.random.rand(100)
    df['size'] = pd.Series(size, index = df.index)
    # df['size'] = df['size'].replace(lambda x: x / x.sum())
    return df


def main():
    print('best sorted:', get_news_sentiment_best().head())
    print('worst sorted:', get_news_sentiment_worst().head())
    # print('map:', get_news_sentiment_map().head())


if __name__ == "__main__":
    get_news_sentiment_best()
