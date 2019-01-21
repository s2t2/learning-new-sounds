# adapted from https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py

import speech_recognition as sr

client = sr.Recognizer() # are there config options here?

with sr.Microphone() as mic:
    print("Say something!")
    audio = client.listen(mic) # are there config options here?

with open("microphone-results.flac", "wb") as f:
    f.write(audio.get_flac_data())
