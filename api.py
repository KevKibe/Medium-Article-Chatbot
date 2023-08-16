import os
from flask import Flask, request, jsonify
from main import MediumArticleChatbot
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv('.env')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    url = data.get('url')
    query = data.get('query')
    chat_history = data.get('chat_history', [])

    if not url or not query:
        return jsonify({"error": "URL or query not provided"}), 400

    chatbot = MediumArticleChatbot([url])
    chatbot.setup()

    # Extend the chat history with the previous conversations
    for question, answer in chat_history:
        chatbot.chat_history.append((question, answer))

    result = chatbot.conversation_chain({"question": query, "chat_history": chatbot.chat_history})
    chatbot.chat_history.append((query, result["answer"]))

    return jsonify({"answer": result["answer"]})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))