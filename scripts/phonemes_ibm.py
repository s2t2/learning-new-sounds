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
    voice_model_response = client.create_voice_model(
        "My Custom Model",
        LANG,
        "to get a valid 'customization_id' value..."
    ).get_result()
    breakpoint()
    #> Error: Required parameter 'base_model_name' is missing, Code: 400 , Information: {'warnings': ['Unexpected input parameter(s) [language] detected in the passed JSON'], 'code_description': 'Bad Request'} ...
    print(json.dumps(voice_model_response, indent=2))
    customization_id = voice_model_response["customization_id"]


    response = client.get_word(customization_id=customization_id, word="HELLO WORLD") #>
    print("RESPONSE")
    print(type(response))
except WatsonApiException as ex:
    print(f"ERROR {str(ex.code)}: {ex.message}")
