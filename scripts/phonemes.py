import os

import speech_recognition as sr

AUDIO_FILENAME = os.environ.get("AUDIO_FILENAME", "microphone-results.flac") # or... "brooklyn.flac"
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
