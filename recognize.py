# adapted from: https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-usage-python

from dotenv import load_dotenv
import io
import os
import pdb  # pdb.set_trace()
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

load_dotenv() # recognize GOOGLE_APPLICATION_CREDENTIALS from .env file

CREDENTIALS_FILEPATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

print(f"\nCREDENTIALS FILE: {CREDENTIALS_FILEPATH}\n")

client = speech.SpeechClient()

config = {
    "encoding": "FLAC",
    "sample_rate_hertz": 16000,
    "language_code": "en-US",
    "enable_word_time_offsets": False
}

audio = {
    "uri": "gs://cloud-samples-tests/speech/brooklyn.flac"
}

response = client.recognize(config, audio)

print(f"\nRESPONSE: {type(response)})\n") #> <class 'google.cloud.speech_v1.types.RecognizeResponse'>)
print(f"\nRESULTS: {type(response.results)})\n") #> <class 'google.protobuf.pyext._message.RepeatedCompositeContainer'>)

for result in response.results:
    print(f"\nRESULT: {type(result)})\n") #> <class 'google.cloud.speech_v1.types.SpeechRecognitionResult'>)
    print(f"\nALTERNATIVES: {type(result.alternatives)})\n") #> <class 'google.protobuf.pyext._message.RepeatedCompositeContainer'>)

    for a in result.alternatives:
        print(a)
        #print(f"\n  TRANSCRIPT: '{a.transcript.title()}' | CONFIDENCE: {a.confidence}\n") #> TRANSCRIPT: 'How Old Is The Brooklyn Bridge' | CONFIDENCE: 0.9833518266677856
