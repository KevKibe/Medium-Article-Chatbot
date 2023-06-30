import os
import sys
from scraping import ArticleFetcher
from query_utils import ConversationChain
from dotenv import load_dotenv
load_dotenv('.env')

class MediumArticleChatbot:
    def __init__(self, urls):
        self.urls = urls
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.conversation = ConversationChain(self.openai_api_key)
        self.chat_history = []
        self.vectorstore = None
        self.conversation_chain = None

    def fetch_and_preprocess_articles(self):
        fetcher = ArticleFetcher(self.urls)
        fetcher.fetch_articles()
        articles = fetcher.get_articles()
        preprocessed_articles = []
        for article in articles:
            preprocessed_text = self.conversation.preprocess_text(article['content'])
            preprocessed_articles.append(preprocessed_text)
        return preprocessed_articles

    def get_text_chunks(self, preprocessed_articles):
        text_chunks = []
        for preprocessed_text in preprocessed_articles:
            chunks = self.conversation.get_text_chunks(preprocessed_text)
            text_chunks.extend(chunks)
        return text_chunks

    def setup(self):
        load_dotenv('.env')
        preprocessed_articles = self.fetch_and_preprocess_articles()
        text_chunks = self.get_text_chunks(preprocessed_articles)
        self.vectorstore = self.conversation.get_vectorstore(text_chunks)
        self.conversation_chain = self.conversation.get_conversation_chain(self.vectorstore)

    def run(self):
        yellow = "\033[0;33m"
        green = "\033[0;32m"
        white = "\033[0;39m"
        print(f"{yellow}---------------------------------------------------------------------------------")
        print('Start your chat-based interaction with your articles')
        print('---------------------------------------------------------------------------------')
        while True:
            query = input(f"{green}Prompt: ")
            if query == "exit" or query == "quit" or query == "q" or query == "f":
                print('\033[32m' + 'Exiting')
                sys.exit()
            if query == '':
                continue
            result = self.conversation_chain({"question": query, "chat_history": self.chat_history})
            print(f"{white}Answer: " + result["answer"])
            self.chat_history.append((query, result["answer"]))

if __name__ == '__main__':
    urls = [
        'https://medium.com/@TechTalkWithAlex/creating-your-first-ever-recommendation-system-like-netflix-5a30e7c461a3',
        'https://medium.com/gitconnected/different-approaches-for-building-recommender-systems-using-python-1bd2179fdc8a',
    ]
    chatbot = MediumArticleChatbot(urls)
    chatbot.setup()
    chatbot.run()
