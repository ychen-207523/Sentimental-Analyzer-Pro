import json
import requests
from bs4 import BeautifulSoup
from newspaper import Article, Config

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"

def scrapNews(topicName):
    article_list = []
    response = getNewsData(topicName)
    results = response.json().get("items", [])

    for result in results:
        link = result.get("link")

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        config = Config()
        config.browser_user_agent = user_agent

        article = Article(link, config=config)
        article.download()
        article.parse()
        article.nlp()
        dict = {}
        if article.summary[:2] != "Ad":
            dict['Summary'] = article.summary
            article_list.append(dict)

    with open('sentimental_analysis/realworld/news.json', 'w') as json_file:
        json.dump(article_list, json_file)

    print("Articles saved to news.json")

# This method returns URLs to news websites matching the relevant query
def getNewsResults(query):
    headers = {
        "User-Agent":user_agent
    }

    base_url = f"https://www.google.com/search?q={query}&gl=us&tbm=nws&num=100"
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    news_results = []

    for el in soup.select("div.SoaBEf"):
        news_results.append(el.find("a")["href"])
    return news_results