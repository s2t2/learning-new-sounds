# adapted from: https://stackoverflow.com/questions/42500907/is-there-a-way-to-return-entire-dictionary-entry-word-phoneme-in-pocketsphin

import os
from dotenv import load_dotenv
import sphinxbase as sb
import pocketsphinx as ps

load_dotenv()

# AUDIO_FILENAME = os.environ.get("AUDIO", "brooklyn.flac")
# AUDIO_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "sounds", AUDIO_FILENAME)
# print("AUDIO FILE:", AUDIO_FILEPATH.replace("scripts/../",""))

PS_DIR = os.environ.get("PS_DIR", "/usr/local/Cellar/cmu-pocketsphinx/HEAD-3bf4fe6/share/pocketsphinx")
MODEL_DIR = os.path.join(PS_DIR, "model") #> "deps/pocketsphinx/model"
DATA_DIR = os.path.join(PS_DIR, "test", "data") #> "deps/pocketsphinx/test/data"
print(MODEL_DIR)
print(DATA_DIR)

config = ps.Decoder.default_config()
config.set_string('-hmm', os.path.join(MODEL_DIR, "en-us/en-us"))
config.set_string('-lm', os.path.join(MODEL_DIR, "en-us/en-us.lm.bin"))
config.set_string('-dict', os.path.join(MODEL_DIR, "en-us/cmudict-en-us.dict"))
print("CONFIG:", type(config))

decoder = ps.Decoder(config)
print("DECODER:", type(decoder))

print("READING AUDIO FILE...")
# can replace this with higher-level speech_recognition package capabilities?
decoder.start_utt()
stream = open(os.path.join(DATA_DIR, "hello_world.wav"), "rb") #> FileNotFoundError: [Errno 2] No such file or directory: '/usr/local/Cellar/cmu-pocketsphinx/HEAD-3bf4fe6/share/pocketsphinx/test/data/hello_world.wav'
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
decoder.end_utt()
stream.close()

print("WORDS:", [seg.word for seg in decoder.seg()])

#print ("PHONEMES:" , [(seg.word, decoder.lookup_word(seg.word)) for seg in decoder.seg()])

breakpoint()
