# adapted from: https://cloud.google.com/speech-to-text/docs/automatic-punctuation

import io
from dotenv import load_dotenv
import os
from google.cloud import speech_v1p1beta1 as speech

LANG = "en-US"
AUDIO_FILENAME = os.environ.get("AUDIO_FILENAME", "brooklyn.flac") # random.shuffle(["brooklyn.flac", "french.aiff" "chinese.flac"])
AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)

load_dotenv() # recognize environment variables from .env file

print("--------------------------")
CREDENTIALS_FILEPATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
print(f"CREDENTIALS FILE: {os.path.isfile(CREDENTIALS_FILEPATH)}")

client = speech.SpeechClient()

config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC, # .LINEAR16 # "must match"
    sample_rate_hertz= 16000, # 8000, # "must match the value in the FLAC header (16000)""
    language_code=LANG,
    enable_automatic_punctuation=True
)





#import speech_recognition as sr
#
#client = sr.Recognizer()
#
#with sr.AudioFile(AUDIO_FILEPATH) as source:
#    audio = client.record(source)



print("READING AUDIO FILE...")

with io.open(AUDIO_FILEPATH, "rb") as audio_file:
    content = audio_file.read()

audio = speech.types.RecognitionAudio(content=content)

print("RECOGNIZING AUDIO...")

response = client.recognize(config, audio)

print("RESPONSE...", type(response))

#breakpoint()

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("------------------------------------------")
    print(f"First alternative of result {i}")
    print(f"Transcript: {alternative.transcript}")
