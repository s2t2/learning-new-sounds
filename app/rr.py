# record and recognize
# adapted from https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py
from os import path
import pdb # pdb.set_trace()
import random
import speech_recognition as sr

AUDIO_FILE = path.join(path.dirname(__file__), "..", "sounds", "brooklyn.flac") # path.join(SOUNDS_DIR, random.shuffle(["brooklyn.flac", "french.aiff" "chinese.flac"]))

client = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = client.record(source)

try:
    print("Sphinx thinks you said " + client.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
