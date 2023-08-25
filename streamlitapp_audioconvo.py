from transcription import SpeechRecognition
import requests
import time
import streamlit as st
from elevenlabs import generate, play, set_api_key
set_api_key(" ")


class TextToSpeech_st:

    def generate_and_play_audio(self, text):
        audio = generate(
            text=text,
            voice="Bella",
            model="eleven_monolingual_v1"
        )
        play(audio)


class Conversation_st:
    def __init__(self):
        self.speech_recognition = SpeechRecognition()
        self.speech_generation = TextToSpeech_st()
        self.url = None
        self.query = None

    def record_and_transcribe(self):
        audio_data = self.speech_recognition.record_audio()
        self.query = self.speech_recognition.transcribe_audio(audio_data)

    def process_query(self):
        if self.query:
            payload = {"url": self.url, "query": self.query}
            response = requests.post("http://3.253.153.46:8080/chat", json=payload)
            response_data = response.json()
            answer = response_data.get("answer")
            self.speech_generation.generate_and_play_audio(answer)

    def run(self):
        st.title("Query an Article")
        self.url = st.text_input("Enter the URL of the Medium article:", key="initial_url")
        record_button = st.button("Click to Speak")
        
        if record_button:
            self.record_and_transcribe()

        if self.query is not None:
            st.write("Your Query:", self.query)
            self.process_query()
            st.write("Click the button to ask another question")

convo = Conversation_st()
convo.run()