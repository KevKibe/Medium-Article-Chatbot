import openai
import nltk
import re
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
openai.api_key = ' '

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]|[\d]', '', text)
    tokens = word_tokenize(text)
    text = ' '.join(tokens)
    return text

def query_articles(text):
    user_prompt = input("Enter your prompt: ")
    prompt = f"Execute this prompt: {user_prompt}: on{text}"
    response = openai.Completion.create(model="gpt-3.5-turbo", prompt=prompt, max_tokens=4096, temperature=0)
    result = response.choices[0].text.strip()
    return result



