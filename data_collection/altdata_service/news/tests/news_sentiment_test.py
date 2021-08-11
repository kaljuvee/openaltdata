import data_collection.altdata_service.news.util.news_sentiment as news_sentiment
import data_collection.altdata_service.news.util.news_util as news_util


def test_store_company_news():
    company_rss_urls = news_util.load_company_rss_urls()
    print('testing urls:', company_rss_urls)
    # print('getting company news', comopany_news_urls)
    for key, url in company_rss_urls.items():
        news_sentiment.store_company_news(url, key)

def test_store_market_news():
    market_rss_urls = news_util.load_market_rss_urls()
    print('testing urls:', market_rss_urls)
    # print('getting company news', comopany_news_urls)
    for key, url in market_rss_urls.items():
        news_sentiment.store_market_news(url, key)

def main():
    test_store_market_news()
    #test_store_company_news()

if __name__ == "__main__":
    main()