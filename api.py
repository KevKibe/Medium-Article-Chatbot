import os
from flask import Flask, request, jsonify
from main import MediumArticleChatbot
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv('.env')

@app.route('/chat', methods=['POST'])
def chat_api():
    data = request.get_json()
    url = data.get('url')
    query = data.get('query')

    if not url or not query:
        return jsonify({"error": "URL or query not provided"}), 400

    chatbot = MediumArticleChatbot([url])
    chatbot.setup()
    response = chatbot.generate_response(query)
    return jsonify({"answer": response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))