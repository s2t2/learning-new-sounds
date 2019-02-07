import os
from watson_developer_cloud import TextToSpeechV1, WatsonApiException

IBM_API_KEY = os.environ.get("IBM_API_KEY", "OOPS")
IBM_URL = os.environ.get("IBM_PASSWORD", "https://gateway-wdc.watsonplatform.net/text-to-speech/api")
print("CREDENTIALS:", IBM_API_KEY)

client = TextToSpeechV1(iam_apikey=IBM_API_KEY, url=IBM_URL)
print("CLIENT:", type(client))

voices = client.list_voices().get_result()
print(json.dumps(voices, indent=2))

#try:
#    response = client.get_word(customization_id="1", word="HELLO WORLD")
#    print("RESPONSE")
#    print(type(response))
#except WatsonApiException as ex:
#    print(f"ERROR {str(ex.code)}: {ex.message}")
