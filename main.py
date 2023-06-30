import os
import sys
from scraping import ArticleFetcher
from query_utils import ConversationChain
from dotenv import load_dotenv
load_dotenv('.env')

class ArticleChatBot:
    def __init__(self, urls, openai_api_key):
        self.fetcher = ArticleFetcher(urls)
        self.openai_api_key = openai_api_key
        self.conversation = None
        self.chat_history = []

    def fetch_articles(self):
        self.fetcher.fetch_articles()

    def preprocess_articles(self):
        articles = self.fetcher.get_articles()
        self.conversation = ConversationChain(self.openai_api_key)
        self.preprocessed_articles = [
            self.conversation.preprocess_text(article['content'])
            for article in articles
        ]

    def generate_text_chunks(self):
        self.text_chunks = [
            chunk
            for preprocessed_text in self.preprocessed_articles
            for chunk in self.conversation.get_text_chunks(preprocessed_text)
        ]

    def setup_chatbot(self):
        self.fetch_articles()
        self.preprocess_articles()
        self.generate_text_chunks()

    def run_chatbot(self):
        yellow = "\033[0;33m"
        green = "\033[0;32m"
        white = "\033[0;39m"

        print(f"{yellow}---------------------------------------------------------------------------------")
        print('Start your chat-based interaction with your articles')
        print('---------------------------------------------------------------------------------')
        while True:
            query = input(f"{green}Prompt: ")
            if query in ["exit", "quit", "q", "f"]:
                print('\033[32m'+'Exiting')
                sys.exit()
            if not query:
                continue
            result = self.conversation.get_conversation_chain(self.text_chunks, self.chat_history, {"question": query})
            print(f"{white}Answer: " + result["answer"])
            self.chat_history.append((query, result["answer"]))

# URLs of the articles to fetch
urls = [
    'https://medium.com/@TechTalkWithAlex/creating-your-first-ever-recommendation-system-like-netflix-5a30e7c461a3',
    'https://medium.com/gitconnected/different-approaches-for-building-recommender-systems-using-python-1bd2179fdc8a',
]

# OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Create an instance of the ArticleChatBot
chatbot = ArticleChatBot(urls, openai_api_key)

# Setup and run the chatbot
chatbot.setup_chatbot()
chatbot.run_chatbot()
