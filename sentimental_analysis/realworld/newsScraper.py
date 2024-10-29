import json
import requests
from bs4 import BeautifulSoup
from newspaper import Article, Config
import logging
import html

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"


# This method scraps article using google news that match the relevant query and dumps it on news.json file
def scrapNews(topicName):
    article_list = []
    news_results = getNewsResults(topicName)
    config = Config()
    config.browser_user_agent = user_agent
    count = 10

    for url in news_results:
        if count == 0:
            break
        try:
            article = Article(url, config=config, language="en")
            article.download()
            article.parse()

            # NLP on the article
            article.nlp()
            dict = {}

            # Extract summary
            if article.summary != "Please enable JS and disable any ad blocker":
                # Unescape the HTML entities
                dict["Summary"] = html.unescape(article.summary)
                article_list.append(dict)
                count -= 1
            else:
                logging.info(f"Skipping article as it requires JS - {url}")
        except BaseException as e:
            logging.info(
                f"Error occured while extracting summary of article - {url}\nError - {e}"
            )

    with open("sentimental_analysis/realworld/news.json", "w") as json_file:
        json.dump(article_list, json_file)

    logging.warning("Articles saved to news.json")


# This method returns URLs to news websites matching the relevant query
def getNewsResults(query):
    headers = {"User-Agent": user_agent}

    base_url = f"https://www.google.com/search?q={query}&gl=us&tbm=nws&num=100"
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    news_results = []

    for el in soup.select("div.SoaBEf"):
        news_results.append(el.find("a")["href"])
    return news_results
