# adapted from https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

import os
import speech_recognition as sr

client = sr.Recognizer() # are there config options here?

with sr.Microphone() as mic:
    print("Say something!")
    audio = client.listen(mic) # are there config options here?

AUDIO_FILE = os.path.join(os.path.dirname(__file__), "..", "sounds", "microphone-results.flac") # path.join(SOUNDS_DIR, random.shuffle(["brooklyn.flac", "french.aiff" "chinese.flac"]))

with open(AUDIO_FILE, "wb") as f:
    f.write(audio.get_flac_data())
