import db.dbutil.news.dbconfig as dbconfig


def test_get_news_id_query():
    # expect True
    query = dbconfig.get_entity_news_id()
    print('test_get_news_id_query:', query)

def test_get_news_sentiment_best():
    # expect True
    df = dbconfig.get_news_sentiment_best()
    print('test_get_news_sentiment_best df:', df.head(10))

def test_get_news_sentiment_worst():
    # expect True
    df = dbconfig.get_news_sentiment_worst()
    print('test_get_news_sentiment_worst df:', df.head(10))

def test_get_news_sentiment_map():
    # expect True
    df = dbconfig.get_news_sentiment_map()
    print('test_get_news_sentiment_map df:', df.head(10))


def main():
    test_get_news_id_query()
    #test_get_news_sentiment_best()
    #test_get_news_sentiment_worst()
    test_get_news_sentiment_map()

if __name__ == "__main__":
    main()