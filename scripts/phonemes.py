import os

from dotenv import load_dotenv
import speech_recognition as sr

load_dotenv()

def sr_brooklyn():
    AUDIO_FILENAME = os.environ.get("AUDIO", "brooklyn.flac")
    AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)
    print("AUDIO FILE:", AUDIO_FILEPATH.replace("scripts/../",""))
    client = sr.Recognizer()
    print("-----------------------")
    print("CLIENT:", type(client))
    with sr.AudioFile(AUDIO_FILEPATH) as source:
        audio = client.record(source)
    print("-----------------------")
    print("AUDIO:", type(audio))
    response = client.recognize_sphinx(audio) #> 'how old is the Brooklyn Bridge'
    print("-----------------------")
    print("TRANSCRIPT:", response.upper())

def sr_grammars():
    AUDIO_FILENAME = os.environ.get("AUDIO", "en-counting.wav") #> "one, two, three"
    AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)
    GRAMMAR_FILENAME = os.environ.get("GRAMMAR", "counting.gram") #> "one, two, three"
    GRAMMAR_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "grammars", GRAMMAR_FILENAME)

    print("AUDIO FILE:", AUDIO_FILEPATH.replace("scripts/../",""))
    client = sr.Recognizer()
    print("-----------------------")
    print("CLIENT:", type(client))
    with sr.AudioFile(AUDIO_FILEPATH) as source:
        audio = client.record(source)
    print("-----------------------")
    print("AUDIO:", type(audio))

    breakpoint()
    response = client.recognize_sphinx(audio, grammar=GRAMMAR_FILEPATH)

    print("-----------------------")
    print("TRANSCRIPT:", response)
    #> INFO: jsgf.c(709): Defined rule: <counting.g00000>
    #> INFO: jsgf.c(709): Defined rule: <counting.g00001>
    #> INFO: jsgf.c(709): Defined rule: PUBLIC <counting.counting>
    #> INFO: jsgf.c(709): Defined rule: <counting.digit>
    #> INFO: jsgf.c(365): Right recursion <counting.g00001> 2 => 0
    #> INFO: fsg_model.c(208): Computing transitive closure for null transitions
    #> INFO: fsg_model.c(270): 0 null transitions added
    #> INFO: fsg_model.c(843): Writing FSG file '/path/to/learning-new-sounds/grammars/counting.fsg'

def spx_brooklyn():
    AUDIO_FILENAME = os.environ.get("AUDIO", "brooklyn.flac")
    AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)
    print("AUDIO FILE:", AUDIO_FILEPATH.replace("scripts/../",""))
    # ...

if __name__ == "__main__":
    sr_grammars()
