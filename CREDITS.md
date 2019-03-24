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
