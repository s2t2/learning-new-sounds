import os

import speech_recognition as sr

AUDIO_FILENAME = os.environ.get("AUDIO_FILENAME", "microphone-results.flac") # or... "brooklyn.flac"
AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)

client = sr.Recognizer()
print("CLIENT:", type(client))

with sr.AudioFile(AUDIO_FILEPATH) as source:
    audio = client.record(source)
print("AUDIO:", type(audio), AUDIO_FILEPATH)

try:
    transcript = client.recognize_google(audio) #> 'how old is the Brooklyn Bridge'
    print("TRANSCRIPT:", transcript)
except Exception as e:
    print("TRANSCRIPT ERROR:", e)
