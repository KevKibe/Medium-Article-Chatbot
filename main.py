import os
from scraping import ArticleFetcher
from query_utils import ConversationChain
from dotenv import load_dotenv
load_dotenv()

urls = [
    'https://medium.com/@TechTalkWithAlex/creating-your-first-ever-recommendation-system-like-netflix-5a30e7c461a3',
    'https://medium.com/gitconnected/different-approaches-for-building-recommender-systems-using-python-1bd2179fdc8a',
    'https://medium.com/@username/article-3'
]

fetcher = ArticleFetcher(urls)

fetcher.fetch_articles()

articles = fetcher.get_articles()

print(articles)
openai_api_key = os.getenv('OPENAI_API_KEY')
conversation = ConversationChain(openai_api_key)
preprocessed_articles = []
for article in articles:
    preprocessed_text = conversation.preprocess_text(article['content'])  
    preprocessed_articles.append(preprocessed_text)

print(preprocessed_articles)
text_chunks = conversation.get_text_chunks(preprocessed_text)
vectorstore = conversation.get_vectorstore(text_chunks)
conversation_chain = conversation.get_conversation_chain(vectorstore)

