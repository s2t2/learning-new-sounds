from dotenv import load_dotenv
import os
from watson_developer_cloud import TextToSpeechV1, WatsonApiException

load_dotenv()

API_KEY = os.environ.get("SPEECH_TO_TEXT_APIKEY", "OOPS")
URL = os.environ.get("SPEECH_TO_TEXT_URL", "https://gateway-wdc.watsonplatform.net/text-to-speech/api")
print("API_KEY:", API_KEY)
print("URL:", URL)

client = TextToSpeechV1(iam_apikey=API_KEY, url=URL)
print("CLIENT:", type(client))

#voices = client.list_voices().get_result()
#print(json.dumps(voices, indent=2))

try:
    #response = client.get_word(customization_id="1", word="HELLO WORLD") #> Malformed GUID: '1'
    #response = client.get_word(word="HELLO WORLD") #> get_word() missing 1 required positional argument: 'customization_id'
    #response = client.get_word(customization_id=None, word="HELLO WORLD") #> ValueError: customization_id must be provided
    #response = client.get_word(customization_id="GA", word="HELLO WORLD") #> ERROR 400: Malformed GUID: 'GA'
    response = client.get_word(customization_id="_______", word="HELLO WORLD") #> ERROR 400: Malformed GUID: 'GA'
    print("RESPONSE")
    print(type(response))
except WatsonApiException as ex:
    print(f"ERROR {str(ex.code)}: {ex.message}")
