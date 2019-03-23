import os
from dotenv import load_dotenv
import pocketsphinx as ps

load_dotenv()

AUDIO_FILENAME = os.environ.get("AUDIO", "brooklyn.flac")
AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)
print("AUDIO FILE:", AUDIO_FILEPATH.replace("scripts/../",""))

for phrase in ps.AudioFile(): # where is this audio coming from? how to customize?
    print(phrase) #> "go forward ten meters"

breakpoint()
