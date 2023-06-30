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

           title_element = soup.select_one('h1')
           
           if title_element:
               title = title_element.text
           else:
               title = 'No title available'

           content_element = soup.select_one('article')
           if content_element:
               content = content_element.text
           else:
               content = 'No content available'

           article = {
               'title': title,
               'content': content
           }

           self.articles.append(article)


    def get_articles(self):
        return self.articles

