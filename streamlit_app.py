import streamlit as st
import requests

def main():
    st.title("Medium Article Chatbot")

    url = st.text_input("User: Enter the URL of the Medium article:")
    query = st.text_input("User: Enter your query:")

    if url and query:
        payload = {"url": url, "query": query}
        response = requests.post("http://54.216.44.96:8080/chat", json=payload)

        if response.status_code == 200:
            response_data = response.json()
            answer = response_data.get("answer")
            
            st.text("Chatbot:")
            st.info(answer)
            
    new_query = st.text_input("User: Enter another query:")

    if new_query:
        payload = {"url": url, "query": new_query}
        response = requests.post("http://54.216.44.96:8080/chat", json=payload)

        if response.status_code == 200:
            response_data = response.json()
            answer = response_data.get("answer")
            
            st.text("Chatbot:")
            st.info(answer)

if __name__ == "__main__":
    main()
