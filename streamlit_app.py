import streamlit as st
import requests

def main():
    st.title("Medium Article Chatbot")

    initial_url = st.text_input("Enter the URL of the Medium article:", key="initial_url")
    query = st.text_input("Enter your query:", key="query")

    conversation_data = []  # Store conversation data including URL and queries

    query_count = 0  # Initialize a counter for query keys

    if initial_url and query:
        payload = {"url": initial_url, "query": query}
        response = requests.post("http://3.253.153.46:8080/chat", json=payload)

        if response.status_code == 200:
            response_data = response.json()
            answer = response_data.get("answer")
            
            st.text("Response:")
            st.info(answer)
            
            # Store the URL and query in conversation_data
            conversation_data.append(("User", initial_url))
            conversation_data.append(("User", query))
            conversation_data.append(("Response", answer))

    while True:
        query_count += 1
        query_key = f"query_{query_count}"  # Generate a unique key for each query input

        new_query = st.text_input("Enter your next query (or leave empty to end):", key=query_key)
        if new_query:
            payload = {"url": initial_url, "query": new_query}
            response = requests.post("http://3.253.153.46:8080/chat", json=payload)

            if response.status_code == 200:
                response_data = response.json()
                answer = response_data.get("answer")
                
                st.text("Response:")
                st.info(answer)
                
                # Store the new query and response in conversation_data
                conversation_data.append(("User", new_query))
                conversation_data.append(("Response", answer))
        else:
            break

if __name__ == "__main__":
    main()
