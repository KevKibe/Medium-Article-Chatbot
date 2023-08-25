from elevenlabs import generate, play, set_api_key
set_api_key("2243a5e8cb3807de8854855f04f6ee4c")



class TextToSpeech:

    def generate_and_play_audio(self, text):
        audio = generate(
            text=text,
            voice="Bella",
            model="eleven_monolingual_v1"
        )
        play(audio)

# speech_generation = TextToSpeech()
# speech_generation.generate_and_play_audio("Ngumi ni mbwegze")