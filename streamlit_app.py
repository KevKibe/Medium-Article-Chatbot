import streamlit as st
import requests

def main():
    st.title("Medium Article Chatbot")

    url = st.text_input("Enter the URL of the Medium article:")
    query = st.text_input("Enter your query:")

    if url and query:
        payload = {"url": url, "query": query}
        response = requests.post("http://54.216.44.96:8080/chat", json=payload)

        if response.status_code == 200:
            response_data = response.json()
            answer = response_data.get("answer")
            st.write("Response:", answer)
        else:
            st.write("Error occurred while retrieving response from the API")

if __name__ == "__main__":
    main()
