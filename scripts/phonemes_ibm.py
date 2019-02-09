from dotenv import load_dotenv
import json
import os
from watson_developer_cloud import TextToSpeechV1, WatsonApiException

load_dotenv()

API_KEY = os.environ.get("SPEECH_TO_TEXT_APIKEY", "OOPS")
URL = os.environ.get("SPEECH_TO_TEXT_URL", "https://gateway-wdc.watsonplatform.net/text-to-speech/api")
print("API_KEY:", API_KEY)
print("URL:", URL)

client = TextToSpeechV1(iam_apikey=API_KEY, url=URL)
print("CLIENT:", type(client))

LANG = "en-US" # Allowable values: [de-DE, en-US, en-GB, es-ES, es-LA, es-US, fr-FR, it-IT ,ja-JP, pt-BR]

try:

    voice_model_response = client.create_voice_model(name="My Custom Model", language=LANG, description="to get a valid 'customization_id' value...").get_result()
    #> https://github.com/watson-developer-cloud/python-sdk/issues/639
    #> https://stackoverflow.com/questions/54599355/ibm-phoneme-detection-in-python

    #breakpoint()

    customization_id = voice_model_response["customization_id"]
    print(customization_id)

    #response = client.get_word(customization_id=customization_id, word="HELLO WORLD")
    print("RESPONSE")
    #print(type(response))
except WatsonApiException as ex:
    print(f"ERROR {str(ex.code)}: {ex.message}")
