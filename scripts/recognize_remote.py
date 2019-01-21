#
# uses the "google.cloud.speech" package directly, via custom project credentials
#
# recognizes the "brooklyn bridge" remote audio file from google cloud storage
#

from dotenv import load_dotenv
import io
import os
import pdb # pdb.set_trace()
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

#
# SETUP
#

load_dotenv() # recognize environment variables from .env file

print("--------------------------")
CREDENTIALS_FILEPATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
print(f"CREDENTIALS FILE: {os.path.isfile(CREDENTIALS_FILEPATH)}")

print("--------------------------")
lang = "en-US" # TODO: allow experiment admin to select from all available options
print(f"LANGUAGE: {lang}")

word = "Brooklyn" # TODO: get this from the experiment administrator
print(f"WORD: {word}")

GCS_BUCKET_DIR = os.environ.get("GCS_BUCKET_DIR", default="cloud-samples-tests/speech")
audio_uri = f"gs://{GCS_BUCKET_DIR}/brooklyn.flac" # TODO: capture audio from user and upload to cloud storage
print(f"AUDIO FILE: {audio_uri}")

#
# CLIENT
#

client = speech.SpeechClient()

#
# REQUEST
#

audio = {"uri": audio_uri}

config = {
    "encoding": "FLAC",
    "sample_rate_hertz": 16000,
    "language_code": lang,
    "enable_word_time_offsets": False # consider exploring differences between setting True vs. False
}

response = client.recognize(config, audio)

#
# PARSED RESPONSE
#

# print(f"\nRESPONSE: {type(response)})") #> <class 'google.cloud.speech_v1.types.RecognizeResponse'>)

for result in response.results:
    # print(f"RESULT: {type(result)})") #> <class 'google.cloud.speech_v1.types.SpeechRecognitionResult'>)

    print("--------------------------")
    for a in result.alternatives:
        print(f"TRANSCRIPT: '{a.transcript.upper()}'") #> TRANSCRIPT: 'How Old Is The Brooklyn Bridge' | CONFIDENCE: 0.9833518266677856
        print(f"CONFIDENCE: {a.confidence}") #> TRANSCRIPT: 'How Old Is The Brooklyn Bridge' | CONFIDENCE: 0.9833518266677856
        if word in a.transcript:
            print(f"DETECTED '{word.upper()}' WITH {a.confidence} CONFIDENCE")
        else:
            print(f"OH, DIDN'T DETECT '{word.upper()}'")
        print("--------------------------")
