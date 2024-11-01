import logging
import unittest
import os, sys
import inspect

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import json
from newsScraper import scrapNews, getNewsResults
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

query = "Artificial Intelligence"
search_for = ["ai", "artificial", "intelligence"]
json_path = r"sentimental_analysis/realworld/news.json"
news_url_json = r"sentimental_analysis/realworld/__tests__/news_url.json"


def urlValidator(url: str) -> bool:
    val = URLValidator()
    try:
        val(url)
        return True
    except (ValidationError,) as e:
        logging.warning(f'Invalid url - {url}')
        return False


class TestNewsResults(unittest.TestCase):
    setup_done = False

    @classmethod
    def setUpClass(self):
        if self.setup_done == True:
            return
        getNewsResults(query, 100)
        with open(news_url_json, "r") as json_file:
            self.news_result_hundred = json.load(json_file)

        self.news_result_one = self.news_result_hundred[:1]
        self.news_result_ten = self.news_result_hundred[:10]
        self.setup_done = True

    def test_query(self):
        response = self.news_result_one
        self.assertNotEqual(response, None)

    def test_query_count_one(self):
        response = self.news_result_one
        self.assertEqual(len(response), 1)

    def test_query_count_multiple(self):
        response = self.news_result_hundred
        self.assertGreater(len(response), 50)

    def test_response_url(self):
        response_url = self.news_result_one[0]
        self.assertTrue(urlValidator(response_url))

    def test_response_url_multiple(self):
        response_url_list = self.news_result_ten

        for url in response_url_list:
            self.assertTrue(urlValidator(url))

    def test_news_results_args(self):
        self.assertTrue(len(inspect.getfullargspec(getNewsResults).args), 2)

    def test_response_relevancy(self):
        response_url = str(self.news_result_one[0]).lower()
        self.assertTrue(urlValidator(response_url))


class TestScrapNews(unittest.TestCase):
    setup_done = False

    @classmethod
    def setUpClass(self):
        if self.setup_done == True:
            return
        with open(json_path, "r") as json_file:
            self.json_data = json.load(json_file)
        self.news = []
        for item in self.json_data:
            self.news.append(item["Summary"])
        self.article_list_single = self.news[:1]
        self.article_list_multiple = self.news
        self.setup_done = True

    def test_query(self):
        self.assertNotEqual(self.article_list_single, None)

    def test_count_one(self):
        self.assertEqual(len(self.article_list_single), 1)

    def test_count_multiple(self):
        self.assertGreater(len(self.article_list_multiple), 5)

    def test_article_validity_JS(self):
        for article in self.article_list_multiple:
            self.assertNotEqual(article, "Please enable JS and disable any ad blocker")

    def test_article_relevancy(self):
        for news in self.news:
            if any(keyword in news for keyword in search_for) == False:
                logging.warning(news)
            self.assertTrue(any(keyword in news.lower() for keyword in search_for))

    def test_scrape_news_args(self):
        self.assertTrue(len(inspect.getfullargspec(scrapNews).args), 3)

    def test_json_dump(self):
        self.assertNotEqual(self.json_data, None)

    def test_json_dump_len(self):
        self.assertGreater(len(self.news), 5)

    def test_json_dump_data_len(self):
        self.assertGreater(len(self.news), 5)

    def test_json_dump_data_validity_JS(self):
        for news in self.news:
            self.assertGreaterEqual(len(news), 250)

    def test_json_dump_relevancy(self):
        for news in self.news:
            if any(keyword in news for keyword in search_for) == False:
                logging.warning(news)
                self.assertTrue(any(keyword in news.lower() for keyword in search_for))
    
    @classmethod
    def tearDownClass(self):
        scrapNews(query, 1, True)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestNewsResults("Test news results"))
    suite.addTest(TestScrapNews("Test news scraping"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
