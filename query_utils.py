import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

nltk.download('stopwords')
nltk.download('punkt')

class ConversationChain:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.openai.api_key = openai_api_key

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]|[\d]', '', text)
        tokens = word_tokenize(text)
        text = ' '.join(tokens)
        return text

    def get_text_chunks(self, text):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(text)
        return chunks

    def get_vectorstore(self, text_chunks):
        vectordb = Chroma.from_documents(text_chunks, embedding=OpenAIEmbeddings(openai_api_key=self.openai_api_key))
        return vectordb

    def get_conversation_chain(self, vectorstore):
        llm = ChatOpenAI()

        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain
