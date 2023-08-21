import streamlit as st
import requests
# from transformers import AutoProcessor, BarkModel

# @st.cache(allow_output_mutation=True)
# def download_model():
#     processor = AutoProcessor.from_pretrained("suno/bark")
#     model = BarkModel.from_pretrained("suno/bark")
#     return processor, model

def main():
    st.title("Medium Article Chatbot")

    url = st.text_input("Enter the URL of the Medium article:")
    query = st.text_input("Enter your query:")

    # processor, model = download_model()

    is_conversation_ongoing = True

    while is_conversation_ongoing:
        if url and query:
            payload = {"url": url, "query": query}
            response = requests.post("http://54.216.44.96:8080/chat", json=payload)

            if response.status_code == 200:
                response_data = response.json()
                answer = response_data.get("answer")
                st.write("Response:", answer)

                # Check if the user wants to continue the conversation
                button = st.button("Continue conversation")
                if button:
                    is_conversation_ongoing = True
                else:
                    is_conversation_ongoing = False
            else:
                st.write("Error occurred while retrieving response from the API")
        else:
            st.write("Please enter the URL of the Medium article and your query.")

if __name__ == "__main__":
    main()
