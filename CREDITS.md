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

## Phoneme Detection

  + https://documenter.getpostman.com/view/2675436/speechace-api-calls/6tW8nSr
  + https://www.speechace.com/#api
  + https://cmusphinx.github.io/wiki/phonemerecognition/
  + https://github.com/Uberi/speech_recognition/blob/f89256b9413e4aa22dee0e5241bfcb7dcd3a9161/speech_recognition/__init__.py#L750
  + https://github.com/watson-developer-cloud/python-sdk/blob/master/watson_developer_cloud/text_to_speech_v1.py
  + https://console.bluemix.net/docs/services/speech-to-text/index.html#about
  + https://github.com/watson-developer-cloud/python-sdk
  + https://myibm.ibm.com/dashboard/
  + https://console.bluemix.net/catalog/services/text-to-speech
  + https://cloud.ibm.com/apidocs/text-to-speech?code=python#authentication
  + https://github.com/watson-developer-cloud/python-sdk#iam
  + https://cloud.ibm.com/docs/services/watson/getting-started-iam.html#iam
  + https://cloud.ibm.com/docs/services/watson/getting-started-iam.html#iamtoken
  + https://cloud.ibm.com/docs/services/watson/apikey-bp.html#api-key-bp
