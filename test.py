import requests

# Replace this URL with the actual URL where your Flask API is running
API_URL = 'http://127.0.0.1:8080/chat'

def test_chat_api():
    url = "https://medium.com/@ErincYigit/linkedin-authentication-and-fetching-user-data-from-api-b820835471c8"
    query = "How does LinkedIn authentication work?"

    # Send a POST request to the API with the URL and query in the JSON payload
    response = requests.post(API_URL, json={'url': url, 'query': query})

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        answer = data.get('answer')
        print(f"URL: {url}")
        print(f"Query: {query}")
        print(f"Answer: {answer}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':
    test_chat_api()
