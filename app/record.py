# adapted from https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

with open("microphone-results.flac", "wb") as f:
    f.write(audio.get_flac_data())
