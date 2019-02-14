from dotenv import load_dotenv
import json
import os
from watson_developer_cloud import TextToSpeechV1, WatsonApiException

load_dotenv()

API_KEY = os.environ.get("TEXT_TO_SPEECH_APIKEY")
URL = os.environ.get("TEXT_TO_SPEECH_URL", "https://gateway-wdc.watsonplatform.net/text-to-speech/api")
CUSTOMIZATION_ID = os.environ.get("CUSTOMIZATION_ID")
LANG = "en-US" # Allowable values: [de-DE, en-US, en-GB, es-ES, es-LA, es-US, fr-FR, it-IT ,ja-JP, pt-BR]
print("API_KEY:", API_KEY)
print("URL:", URL)
print("CUSTOMIZATION_ID:", CUSTOMIZATION_ID)
print("LANG:", LANG)

client = TextToSpeechV1(iam_apikey=API_KEY, url=URL)
print("CLIENT:", type(client)) #> <class 'watson_developer_cloud.text_to_speech_adapter_v1.TextToSpeechV1Adapter'>

def get_customization_id():
    if CUSTOMIZATION_ID:
        print("DETECTED EXISTING VOICE MODEL...")
        return CUSTOMIZATION_ID
    else:
        print("CREATING CUSTOM VOICE MODEL...")
        voice_model_response = client.create_voice_model(
            name="My Custom Model",
            language=LANG,
            description="to get a valid 'customization_id' value..."
        ).get_result()
        new_id = voice_model_response["customization_id"]
        print("NEW CUSTOMIZATION_ID:", new_id)
        return new_id

try:
    customization_id = get_customization_id()
    response = client.get_word(customization_id=customization_id, word="HELLO WORLD")
    #> ERROR 400: Word 'HELLO WORLD' not found in custom model 'abc-123'
    print("RESPONSE")
    print(type(response))
except WatsonApiException as ex:
    print(f"ERROR {str(ex.code)}: {ex.message}")
