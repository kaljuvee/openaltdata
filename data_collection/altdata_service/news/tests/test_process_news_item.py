import unittest
import data_collection.altdata_service.news.util.process_news_item as nip
import data_collection.altdata_service.news.tests.unit_test_data as test_data


class TestingProcessingOfNewsItem(unittest.TestCase):
    def test_process_item(self):
        for news_item_input, news_item_output in zip(test_data.news_items, test_data.news_items_outputs):
            article_dict = nip.NewsItemProcessor(news_item_input, '', '').process_item()
            self.assertListEqual(article_dict, news_item_output)


if __name__ == '__main__':
    unittest.main()
