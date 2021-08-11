import unittest
import data_collection.altdata_service.news.util.ticker_extractor as tx
import data_collection.altdata_service.news.tests.unit_test_data as test_data
import re
import math
from collections import Counter


def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


def get_result(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


class TestTickerExtractor(unittest.TestCase):

    def test_extractor(self):
        for test_IO in test_data.test_list:
            input_params = test_IO['input']
            output = test_IO['output']

            extractor = tx.TickerExtractor(
                summary=input_params['summary'],
                link=input_params['link'],
                unprocessed_ticker=input_params['u_ticker']
            )
            extractor.process_arguments()

            u_ticker_list = extractor.unprocessed_ticker_list
            ticker_list = extractor.ticker_list
            exchange_list = extractor.exchange_list
            ticker_normal_list = extractor.ticker_normal_list

            self.assertEqual(set(u_ticker_list), set(output['unprocessed_ticker_list']))
            self.assertEqual(set(ticker_list), set(output['ticker_list']))
            self.assertEqual(set(exchange_list), set(output['exchange_list']))
            self.assertEqual(set(ticker_normal_list), set(output['ticker_normal_list']))
            self.assertEqual(extractor.found_ticker_with_trit_api, output['found_ticker_with_trit_api'])

    def test_trit_api_func(self):
        for summary, output in zip(test_data.test_text['summaries'], test_data.test_text['outputs']):
            ticker_list = tx.TickerExtractor().extract_ric_from_text(text=summary)
            self.assertEqual(set(ticker_list), set(output))

    def test_article_body_extraction_from_url(self):
        for url, body in zip(test_data.test_urls['urls'], test_data.test_urls['bodies']):
            body_from_url = tx.TickerExtractor().get_text_from_link(url)
            percentage = get_result(body_from_url, body)
            self.assertGreater(percentage, 0.8)


if __name__ == '__main__':
    unittest.main()
