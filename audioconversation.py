from transcription import SpeechRecognition
from audio_gen import TextToSpeech
import requests
import time

speech_recognition = SpeechRecognition()
speech_generation = TextToSpeech()

class Conversation:
    def __init__(self, url):
        self.url = url

    def record_and_transcribe_audio(self):
        audio_data = speech_recognition.record_audio()
        query = speech_recognition.transcribe_audio(audio_data)
        return query

    def send_query_to_server(self, query):
        payload = {"url": self.url, "query": query}
        response = requests.post("http://3.253.153.46:8080/chat", json=payload)
        response_data = response.json()
        answer = response_data.get("answer")
        return answer

    def run(self):
        while True:
            query = self.record_and_transcribe_audio()
            print("User query:", query)

            start_time = time.time()
            answer = self.send_query_to_server(query)
            print("Response:", answer)

            end_time = time.time()

            speech_generation.generate_and_play_audio(answer)

            elapsed_time = end_time - start_time
            print(f"Time: {elapsed_time:.2f} seconds\n")

url = "https://thebolditalic.com/why-im-breaking-up-with-burning-man-efe43bb5c9c5"

convo = Conversation(url)
convo.run()



