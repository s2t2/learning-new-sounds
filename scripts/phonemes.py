import os

from dotenv import load_dotenv
import speech_recognition as sr

load_dotenv()

AUDIO_FILENAME = os.environ.get("AUDIO", "brooklyn.flac")
AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)

print("AUDIO FILE:" + AUDIO_FILEPATH.replace("scripts/../",""))

client = sr.Recognizer()

print("-----------------------")
print("CLIENT:", type(client))

with sr.AudioFile(AUDIO_FILEPATH) as source:
    audio = client.record(source)

print("-----------------------")
print("AUDIO:", type(audio))

response = client.recognize_sphinx(audio) #> 'how old is the Brooklyn Bridge'

print("-----------------------")
print("RESPONSE:", type(response))
print("TRANSCRIPT:", response)
