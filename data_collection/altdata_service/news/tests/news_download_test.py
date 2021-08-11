import data_collection.altdata_service.news.news_download as news_download


def test_check_news_item():
    link = 'http://www.globenewswire.com/news-release/2020/05/11/2031537/0/en/Lamar-Advertising-Company-Prices-Private-Offering-of-Senior-Notes.html'
    # expect True
    print('check news item', news_download.check_news_item(link))

def test_load_rss_urls():
    news_download.load_rss_urls()

def main():
    test_load_rss_urls()
    test_check_news_item()

if __name__ == "__main__":
    main()