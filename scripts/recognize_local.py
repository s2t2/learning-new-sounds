#
# uses the "speech_recognition" package (which uses Google Cloud Speech API via demo credentials)
#
# recognizes the "brooklyn bridge" local audio file
#

import os
import pdb # pdb.set_trace()
import random
import speech_recognition as sr


AUDIO_FILENAME = os.environ.get("AUDIO_FILENAME", "brooklyn.flac") # random.shuffle(["brooklyn.flac", "french.aiff" "chinese.flac"])
AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)

#pdb.set_trace()

client = sr.Recognizer()

with sr.AudioFile(AUDIO_FILEPATH) as source:
    audio = client.record(source)

try:
    #transcript = client.recognize_google(audio) #> 'how old is the Brooklyn Bridge'
    #print("TRANSCRIPT: " + transcript)

    response = client.recognize_google(audio, show_all=True) #> {'alternative': [{'transcript': 'how old is the Brooklyn Bridge', 'confidence': 0.987629}], 'final': True}
    alternative = response["alternative"][0]
    print("TRANSCRIPT: " + alternative["transcript"])
    print("CONFIDENCE: " + str(alternative["confidence"]))

except Exception as e:
    print("TRANSCRIPT ERROR:", e)
