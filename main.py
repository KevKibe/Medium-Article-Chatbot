import os
import sys
from scraping import ArticleFetcher
from query_utils import ConversationChain
from dotenv import load_dotenv
load_dotenv('.env')

urls = [
    'https://medium.com/@TechTalkWithAlex/creating-your-first-ever-recommendation-system-like-netflix-5a30e7c461a3',
    'https://medium.com/gitconnected/different-approaches-for-building-recommender-systems-using-python-1bd2179fdc8a',
    'https://medium.com/@username/article-3'
]

fetcher = ArticleFetcher(urls)

fetcher.fetch_articles()

articles = fetcher.get_articles()

openai_api_key = os.getenv('OPENAI_API_KEY')
conversation = ConversationChain(openai_api_key)
preprocessed_articles = []
for article in articles:
    preprocessed_text = conversation.preprocess_text(article['content'])  
    preprocessed_articles.append(preprocessed_text)

text_chunks = []
for preprocessed_text in preprocessed_articles:
    chunks = conversation.get_text_chunks(preprocessed_text)
    text_chunks.extend(chunks)

vectorstore = conversation.get_vectorstore(text_chunks)
conversation_chain = conversation.get_conversation_chain(vectorstore)

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"

chat_history = []
print(f"{yellow}---------------------------------------------------------------------------------")
print('Welcome to the DocBot. You are now ready to start interacting with your documents')
print('---------------------------------------------------------------------------------')
while True:
    query = input(f"{green}Prompt: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Exiting')
        sys.exit()
    if query == '':
        continue
    result = conversation_chain(
        {"question": query, "chat_history": chat_history})
    print(f"{white}Answer: " + result["answer"])
    chat_history.append((query, result["answer"]))
