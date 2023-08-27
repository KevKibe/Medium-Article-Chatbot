import os
from fastapi import FastAPI, HTTPException
from main import MediumArticleChatbot
from dotenv import load_dotenv
import uvicorn

app = FastAPI()
load_dotenv('.env')

@app.post('/chat')
async def chat_api(data: dict):
    url = data.get('url')
    query = data.get('query')

    if not url or not query:
        raise HTTPException(status_code=400, detail="URL or query not provided")

    chatbot = MediumArticleChatbot([url])
    chatbot.setup()
    response = chatbot.generate_response(query)
    return {"answer": response}

if __name__ == '__main__':
    
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
