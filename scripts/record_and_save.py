import os
import speech_recognition as sr
import pdb # pdb.set_trace()
import random

AUDIO_FILENAME = os.environ.get("AUDIO_FILENAME", "microphone-results.flac") # random.shuffle(["brooklyn.flac", "french.aiff" "chinese.flac"])
AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)

def main():

	client = sr.Recognizer() # are there config options here?

	#
	# READ AUDIO FROM MICROPHONE
	#

	with sr.Microphone() as mic:
	    print("Say something!")
	    audio = client.listen(mic) # are there config options here?

	#
	# WRITE AUDIO TO FILE
	#

	with open(AUDIO_FILEPATH, "wb") as f:
	    f.write(audio.get_flac_data())

	#
	# RECOGNIZE WHAT WAS SAID
	#

	client = sr.Recognizer()

	# with sr.AudioFile(AUDIO_FILEPATH) as source:
	#     audio = client.record(source)

	try:
	    #transcript = client.recognize_google(audio) #> 'how old is the Brooklyn Bridge'
	    #print("TRANSCRIPT: " + transcript)

	    response = client.recognize_google(audio, show_all=True) #> {'alternative': [{'transcript': 'how old is the Brooklyn Bridge', 'confidence': 0.987629}], 'final': True}
	    alternative = response["alternative"][0]
	    print("TRANSCRIPT: " + alternative["transcript"])
	    print("CONFIDENCE: " + str(alternative["confidence"]))

	except Exception as e:
	    print("TRANSCRIPT ERROR:", e)

if __name__ == '__main__':
	main()
