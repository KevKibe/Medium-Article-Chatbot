import requests
from bs4 import BeautifulSoup

class ArticleFetcher:
    def __init__(self, urls):
        self.urls = urls
        self.articles = []

    def fetch_articles(self):
        for url in self.urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            title = soup.select_one('h1').text
            content = soup.select_one('article').text

            article = {
                'title': title,
                'content': content
            }

            self.articles.append(article)

    def get_articles(self):
        return self.articles
