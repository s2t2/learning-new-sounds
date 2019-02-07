import os
from watson_developer_cloud import TextToSpeechV1

#API_KEY = os.environ.get("IBM_API_KEY", "OOPS")

#text_to_speech = TextToSpeechV1(
#    iam_apikey= API_KEY,
#    url=''
#)

IBM_USERNAME = os.environ.get("IBM_USERNAME", "OOPS")
IBM_PASSWORD = os.environ.get("IBM_PASSWORD", "OOPS")
IBM_URL = "https://gateway-wdc.watsonplatform.net/text-to-speech/api"

client = TextToSpeechV1(
    username= IBM_USERNAME,
    password= IBM_PASSWORD,
    url=IBM_URL
)

print(type(client))

breakpoint()

try:
    client.get_word(customization_id="1", word="HELLO WORLD")
except WatsonApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message
