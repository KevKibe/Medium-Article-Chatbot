from transcription import SpeechRecognition
from audio_gen import TextToSpeech
from main import MediumArticleChatbot
import requests
import time

speech_recognition = SpeechRecognition()
speech_generation = TextToSpeech()


class Conversation:
    def __init__(self, url):
        self.urls = url

    def record_and_transcribe_audio(self):
        audio_data = speech_recognition.record_audio()
        query = speech_recognition.transcribe_audio(audio_data)
        return query

    def get_response(self, query):
        chatbot = MediumArticleChatbot(self.urls)
        chatbot.setup()
        response = chatbot.generate_response(query)
        return response

    def run(self):
        while True:
            query = self.record_and_transcribe_audio()
            print("User query:", query)

            start_time = time.time()
            answer = self.get_response(query)
            print("Response:", answer)

            end_time = time.time()

            speech_generation.generate_and_play_audio(answer)

            elapsed_time = end_time - start_time
            print(f"Time: {elapsed_time:.2f} seconds\n")

url = ["https://medium.com/backenders-club/api-design-best-practices-a-deep-dive-2022-ec5a19dc27cc",
       "https://medium.com/javarevisited/10-rest-api-best-practices-cd12e3904d00"]

convo = Conversation(url)
convo.run()



