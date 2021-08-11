import data_collection.altdata_service.news.util.news_util as news_util
import feedparser

news_urls = {'globenewswire-us': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
             'globenewswire-ma': 'https://www.globenewswire.com/RssFeed/subjectcode/27-Mergers%20And%20Acquisitions/feedTitle/GlobeNewswire%20-%20Mergers%20And%20Acquisitions'}

def test_check_news_item():
    link = 'http://www.globenewswire.com/news-release/2020/05/11/2031537/0/en/Lamar-Advertising-Company-Prices-Private-Offering-of-Senior-Notes.html'
    # expect True
    print('check news link', news_util.check_news_item(link))

def test_get_ticker():
    for key, url in news_urls.items():
        feed = feedparser.parse(url)
        for newsitem in feed['items']:
            print('newsitem link:', newsitem['link'])
            print('newsitem ticker:', news_util.get_ticker(newsitem))
            print('newsitem ticker source:', news_util.get_ticker_source(newsitem))

def test_get_yticker():
    for key, url in news_urls.items():
        feed = feedparser.parse(url)
        for newsitem in feed['items']:
            #print('newsitem link:', newsitem['link'])
            print('newsitem yticker:', news_util.get_yticker(newsitem))


def main():
    test_check_news_item()
    test_get_ticker()
    test_get_yticker()
    #test_get_trading_session()

if __name__ == "__main__":
    main()