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
