import logging
import unittest
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import json
from newsScraper import scrapNews, getNewsResults
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

query = "Artificial Intelligence"
search_for = ["ai", "artificial", "intelligence"]
json_path = r"sentimental_analysis/realworld/news.json"


def urlValidator(url: str) -> bool:
    val = URLValidator()
    try:
        val(url)
        return True
    except (ValidationError,) as e:
        return False


class TestNewsResults(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.news_result_one = getNewsResults(query, 1)
        self.news_result_ten = getNewsResults(query, 10)
        self.news_result_hundred = getNewsResults(query, 100)

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
        response_url_list = self.news_result_ten[0]

        for url in response_url_list:
            if urlValidator(url) == False:
                print(url)
            self.assertTrue(urlValidator(url))

    def test_response_relevancy(self):
        response_url = str(self.news_result_one[0]).lower()
        self.assertTrue(urlValidator(response_url))


class TestScrapNews(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.article_list_single = scrapNews(query, 1, False)
        self.article_list_multiple = scrapNews(query, 10, False)
        with open(json_path, "r") as json_file:
            self.json_data = json.load(json_file)
        self.news = []
        for item in self.json_data:
            self.news.append(item["Summary"])

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


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestNewsResults("Test news results"))
    suite.addTest(TestScrapNews("Test news scraping"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
