import json
import os
import yaml
from bs4 import BeautifulSoup
import feedparser
import requests
import logging

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
GNW_EOD_PATH = os.path.join(ABS_PATH, '../config', 'globenewswire_eodhistorical.yaml')
logging.basicConfig(level=logging.INFO)

with open(GNW_EOD_PATH) as yaml_file:
    exchanges = yaml.full_load(yaml_file)


class TickerExtractor:
    """Processes given arguments and extracts ticker, exchange and ticker_normal"""

    # Only one argument is required, for instance if only summary is given as argument
    # then only summary will be processed

    # Argument processing priority: 1. unprocessed_ticker 2. summary 3. link
    # For example if all arguments are given and ticker can be extracted from unprocessed_ticker,
    # then summary and link will be ignored

    # Functions extract_ric_from_text and get_text_from_link can be used without creating an instance

    def __init__(self, summary=None, link=None, unprocessed_ticker=None):
        self.summary = summary
        self.link = link
        self.unprocessed_ticker_list = [unprocessed_ticker]
        self.ticker_list = []
        self.exchange_list = []
        self.ticker_normal_list = []
        self.found_ticker_with_trit_api = False

    def process_arguments(self):
        if self.unprocessed_ticker_list[0] is not None:
            self.unprocessed_ticker_list[0] = self.unprocessed_ticker_list[0] if '.' in self.unprocessed_ticker_list[
                0] or ':' in self.unprocessed_ticker_list[0] else None
        if (self.summary is not None) and (self.unprocessed_ticker_list[0] is None):
            self.unprocessed_ticker_list = self.extract_ric_from_text(self.summary)
        if (self.link is not None) and (self.unprocessed_ticker_list[0] is None):
            text_from_url = self.get_text_from_link(self.link)
            self.unprocessed_ticker_list = self.extract_ric_from_text(text_from_url)

        self.__set_ticker()
        self.__set_exchange()
        self.__set_ticker_normal()

    def __set_ticker(self):
        for unprocessed_ticker in self.unprocessed_ticker_list:
            if unprocessed_ticker is None:
                self.ticker_list.append(None)
            elif ':' in unprocessed_ticker:
                unprocessed_ticker_as_list = unprocessed_ticker.split(":")
                self.ticker_list.append(unprocessed_ticker_as_list[1].strip())
            elif '.' in unprocessed_ticker:
                unprocessed_ticker_as_list = unprocessed_ticker.split(".")
                self.ticker_list.append(unprocessed_ticker_as_list[0].strip())
            else:
                self.ticker_list.append(None)

    def __set_exchange(self):
        for unprocessed_ticker in self.unprocessed_ticker_list:
            if unprocessed_ticker is None:
                self.exchange_list.append(None)
            elif ':' in unprocessed_ticker:
                unprocessed_ticker_as_list = unprocessed_ticker.split(":")
                self.exchange_list.append(unprocessed_ticker_as_list[0].strip())
            elif '.' in unprocessed_ticker:
                unprocessed_ticker_as_list = unprocessed_ticker.split(".")
                self.exchange_list.append(unprocessed_ticker_as_list[1].strip())
            else:
                self.exchange_list.append(None)

    def __set_ticker_normal(self):
        for exchange_index in range(len(self.exchange_list)):
            if self.exchange_list[exchange_index] in exchanges.keys():
                self.ticker_normal_list.append(
                    self.ticker_list[exchange_index] + " " + exchanges[self.exchange_list[exchange_index]])
            else:
                self.ticker_normal_list.append(None)

    def extract_ric_from_text(self, text):

        trit_api_tokens = ['oSyQfYcRShExGJmJPXRgr4kOFAsIHqoJ', 'YFX4ny5glFWKLMGW4EBd9WVckdvGa5QJ']
        url = "https://api-eit.refinitiv.com/permid/calais"

        payload = text.encode('utf8')

        for retry in range(10):
            try:
                trit_response = requests.request("POST", url, data=payload, headers={
                    'Content-Type': "text/raw",
                    'X-AG-Access-Token': trit_api_tokens[retry % 2],
                    'outputformat': "application/json"
                })
            except requests.exceptions.ChunkedEncodingError:
                continue

            if trit_response.status_code == 413:
                # request exceeds the maximum allowed document size
                # Reducing payload by half
                payload = payload[:len(payload) // 2]

            try:
                json_response = json.loads(trit_response.text)
                break
            except json.decoder.JSONDecodeError:
                if retry == 9:
                    logging.warning("TRIT API ticker extraction failed. URL: " + self.link)
                    return [None]

        ric_list = list(self.__find_primary_ric(json_response, 'primaryric'))

        if len(ric_list):
            self.found_ticker_with_trit_api = True

        return list(dict.fromkeys(ric_list)) if len(ric_list) > 0 else [None]

    def __find_primary_ric(self, start_node, key_value):
        for key in start_node:
            try:
                yield start_node[key]['resolutions'][0][key_value]
            except KeyError:
                continue

    def get_text_from_link(self, url):
        if 'globenewswire' in url:
            feed = feedparser.parse(url)
            try:
                soup = BeautifulSoup(feed['feed']['summary'], 'html.parser')
            except KeyError:
                return ""
            body = soup.find(class_="article-body")

        elif 'businesswire' in url:
            result = requests.get(url)
            c = result.content
            soup = BeautifulSoup(c, 'html.parser')
            body = soup.find("div", {"class": "bw-release-story"})

        elif 'www.newswire.com' in url:
            result = requests.get(url)
            c = result.content
            soup = BeautifulSoup(c, 'html.parser')
            body = soup.find("div", {"class": "html-content clearfix"})

        else:
            body = ''

        if body == '':
            return body
        try:
            content = body.find_all('p')
        except AttributeError:
            return ''

        text = ""
        for tag in content:
            text += tag.text.strip()
        return text
