# adapted from: https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-usage-python

from dotenv import load_dotenv
import io
import os
import pdb
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

load_dotenv() # recognize GOOGLE_APPLICATION_CREDENTIALS from .env file

#pdb.set_trace()

CREDENTIALS_FILEPATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

print("---------------------------")
print(f"CREDENTIALS FILE: {CREDENTIALS_FILEPATH}")
print("---------------------------")

client = speech.SpeechClient()

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US"
)

file_name = os.path.join(os.path.dirname(__file__), "resources", "audio.raw")

with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

response = client.recognize(config, audio)

print("---------------------------")
print(f"RESPONSE (#{type(response)}):")
print("---------------------------")

for result in response.results:
    print( f"Transcript: #{result.alternatives[0].transcript}")
