# Credits, Notes, References

## Google Speech to Text API

  + https://cloud.google.com/speech-to-text/docs/quickstart-protocol


Example `recognize` request:

```sh
curl -s -H "Content-Type: application/json" \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://speech.googleapis.com/v1/speech:recognize \
    -d @sync-request.json
```

## Storing Audio Files

  + https://stackoverflow.com/questions/38806490/what-does-gs-protocol-mean
  + https://storage.googleapis.com/cloud-samples-tests/speech/brooklyn.flac

## Google API Client (Python)

  + https://cloud.google.com/speech-to-text/docs/reference/libraries
  + https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-install-python
  + https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-usage-python
  + https://github.com/googleapis/google-cloud-python
  + https://googleapis.github.io/google-cloud-python/latest/speech/index.html
  + https://pypi.org/project/google-cloud-speech/
  + https://github.com/googleapis/google-cloud-python/tree/master/speech


## Google Cloud SDK

  + https://cloud.google.com/sdk/ (is this necessary?)

## Recording Audio

  + https://github.com/Uberi/speech_recognition
  + http://people.csail.mit.edu/hubert/pyaudio/#downloads
  + https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
  + https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py
  + https://github.com/Uberi/speech_recognition/blob/master/examples
  + https://github.com/Uberi/speech_recognition/blob/master/speech_recognition/__main__.py















<hr>

## Phoneme Recognition

  + https://cmusphinx.github.io/wiki/cmubet/
  + http://www.speech.cs.cmu.edu/cgi-bin/cmudict
  + https://en.wikipedia.org/wiki/ARPABET

```py
"hello" #> HH AH L OW
"world" #> W ER L D
```

### Sphinx

"Recently a support for phoneme recognition has been added to pocketsphinx decoder."


  + https://cmusphinx.github.io/wiki/phonemerecognition/
  + https://cmusphinx.github.io/wiki/pocketsphinx_pronunciation_evaluation/
  + https://cmusphinx.github.io/wiki/
  + https://cmusphinx.github.io/wiki/tutorial/
  + https://cmusphinx.github.io/wiki/download/
  + https://github.com/cmusphinx/pocketsphinx
  + https://stackoverflow.com/questions/35174935/pocketsphinx-install-does-not-contain-acoustic-model-definition-mdef
  + https://github.com/watsonbox/homebrew-cmu-sphinx (2015 old?)
  + https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/
  + https://cmusphinx.github.io/wiki/tutorialpocketsphinx/

```sh
brew tap watsonbox/cmu-sphinx

brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase
brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx
```

```sh
pkg-config --variable=modeldir pocketsphinx
#> /usr/local/Cellar/cmu-pocketsphinx/HEAD-3bf4fe6/share/pocketsphinx/model
```

```sh
cd deps/
git clone git@github.com:cmusphinx/sphinxbase.git
git clone git@github.com:cmusphinx/pocketsphinx.git
```

  + https://bangladroid.wordpress.com/2017/02/16/installing-cmu-sphinx-on-ubuntu/

"Now we need to run the autogen.sh shell script you can see in the sphinxbase directory. This will generate our Makefiles and other important scripts for compiling and installing. We’re going to get a long output here, so I only show some of it here:"

```sh
deps/sphinxbase/autogen.sh
make # oops i ran this from the root directory of this repository. it generated a bunch of files in this repo, which i subsequently deleted
```

not sure how installed, but it is, and the objective is to run something like...

```sh
# sphinx_lm_eval (to test sphinxbase installation)
# pocketsphinx_continuous (to test pocketsphinx installation)

pocketsphinx_continuous -infile deps/pocketsphinx/test/data/goforward.raw
#> go forward ten meters
```

Yeah but how about phoneme recognition?

```sh
pocketsphinx_continuous -infile deps/pocketsphinx/test/data/goforward.raw \
                        -hmm  deps/pocketsphinx/model/en-us/en-us \
                        -allphone deps/pocketsphinx/model/en-us/en-us-phone.lm.bin \
                        -backtrace yes \
                        -beam 1e-20 -pbeam 1e-20 -lw 2.0
#> SIL G OW F AO R D T AE N NG IY ZH ER S SIL
```

Haha ok. what?

``` sh
# http://www.speech.cs.cmu.edu/cgi-bin/cmudict
AA	odd     AA D
AE	at	AE T
AH	hut	HH AH T
AO	ought	AO T
AW	cow	K AW
AY	hide	HH AY D
B 	be	B IY
CH	cheese	CH IY Z
D 	dee	D IY
DH	thee	DH IY
EH	Ed	EH D
ER	hurt	HH ER T
EY	ate	EY T
F 	fee	F IY
G 	green	G R IY N
HH	he	HH IY
IH	it	IH T
IY	eat	IY T
JH	gee	JH IY
K 	key	K IY
L 	lee	L IY
M 	me	M IY
N 	knee	N IY
NG	ping	P IH NG
OW	oat	OW T
OY	toy	T OY
P 	pee	P IY
R 	read	R IY D
S 	sea	S IY
SH	she	SH IY
T 	tea	T IY
TH	theta	TH EY T AH
UH	hood	HH UH D
UW	two	T UW
V 	vee	V IY
W 	we	W IY
Y 	yield	Y IY L D
Z 	zee	Z IY
ZH	seizure	S IY ZH ER
```

```sh
#> G OW
#> F AO R D
#> T AE N
#> NG IY ZH ER S
```

### Sphinx in Python

  + https://pypi.org/project/pocketsphinx/
  + https://github.com/bambocher/pocketsphinx-python
  + https://github.com/bambocher/pocketsphinx-python#audiofile
  + https://stackoverflow.com/questions/42500907/is-there-a-way-to-return-entire-dictionary-entry-word-phoneme-in-pocketsphin


### Speech Recognition in Python

  + https://github.com/Uberi/speech_recognition
  + https://github.com/Uberi/speech_recognition#pocketsphinx-python-for-sphinx-users
  + https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst
  + https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_sphinxaudio_data-audiodata-language-str--en-us-keyword_entries-unioniterabletuplestr-float-none--none-grammar-unionstr-none--none-show_all-bool--false---unionstr-pocketsphinxpocketsphinxdecoder
  + https://github.com/Uberi/speech_recognition/blob/19dc36eb6a6173b500e2cc8cf2161ea2fe8cb891/examples/special_recognizer_features.py
  + https://github.com/Uberi/speech_recognition/blob/19dc36eb6a6173b500e2cc8cf2161ea2fe8cb891/tests/test_special_features.py
  + https://github.com/Uberi/speech_recognition/blob/f89256b9413e4aa22dee0e5241bfcb7dcd3a9161/speech_recognition/__init__.py#L746-L843
  + https://raw.githubusercontent.com/Uberi/speech_recognition/19dc36eb6a6173b500e2cc8cf2161ea2fe8cb891/examples/english.wav

"PocketSphinx-Python is required if and only if you want to use the Sphinx recognizer (recognizer_instance.recognize_sphinx)."

"By default, SpeechRecognition's Sphinx functionality supports only US English. Additional language packs are also available [in ...] International French, Mandarin Chinese, [and] Italian."
