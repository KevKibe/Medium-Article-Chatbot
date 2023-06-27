from scraping import ArticleFetcher
from query_utils import preprocess_text, query_articles
from query_utils import ConversationChain

urls = [
    'https://medium.com/total-data-science/the-exact-steps-i-used-to-become-a-data-scientist-microsoft-3733fd9f75',
    'https://medium.com/@username/article-2',
    'https://medium.com/@username/article-3'
]

fetcher = ArticleFetcher(urls)

fetcher.fetch_articles()

articles = fetcher.get_articles()

for i, article in enumerate(articles):
    print(f'Article {i+1}:')
    print(f'Title: {article["title"]}')
    preprocessed_content = preprocess_text(article["content"])
    query_result = query_articles(preprocessed_content)
    print(f'Query Result: {query_result}')
    print('---')

openai_api_key = 'your_api_key'
conversation = ConversationChain(openai_api_key)

preprocessed_text = conversation.preprocess_text("Your text")
text_chunks = conversation.get_text_chunks(preprocessed_text)
vectorstore = conversation.get_vectorstore(text_chunks)
conversation_chain = conversation.get_conversation_chain(vectorstore)
