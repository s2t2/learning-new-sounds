# Contributor's Guide

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Download or clone from [GitHub source](https://github.com/s2t2/learning-new-sounds).

## Setup

Navigate into this repository:

```sh
cd learning-new-sounds
```

Create and activate a new virtual environment:

```sh
conda create -n sounds-env
conda activate sounds-env
```

Install package dependencies:

```sh
pip install --upgrade google-cloud-speech # only necessary for running script/recognize_remote.py
pip install python-dotenv
pip install pyaudio # on Mac OS, first run: `brew install portaudio` (see http://people.csail.mit.edu/hubert/pyaudio/#downloads)
pip install SpeechRecognition # depends on pyaudio


pip install --upgrade watson-developer-cloud
```

## Authorization

> only necessary for running script/recognize_remote.py ...

Setup a new project in the [Google API Console](https://console.cloud.google.com/cloud-resource-manager), enable the "Cloud Speech API" for this project, and download the corresponding credentials .json file into the "credentials" directory of this repository. Note the full path to this credentials file.

Create a new `.env` file in the root directory of this repository, as a copy of the `env.example` file, and update the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in the new `.env` file to point to the credentials .json filepath.

## Usage

### Audio Recording

Record audio and save to file "sounds/microphone-results.flac":

```sh
python scripts/record.py
```

### Speech Recognition

Recognize speech (reads from "sounds/brooklyn.flac" by default, but possible to customize via `AUDIO_FILENAME` environment variable referencing the name of a file in the "sounds" directory):

```sh
python scripts/recognize_local.py

AUDIO_FILENAME="microphone-results.flac" python scripts/recognize_local.py

AUDIO_FILENAME="el-ninyo.flac" LANG="es" python scripts/recognize_local.py

AUDIO_FILENAME="arigato.flac" LANG="jp" python scripts/recognize_local.py

AUDIO_FILENAME="chinese.flac" LANG="zh" python scripts/recognize_local.py

AUDIO_FILENAME="bulgarian.flac" LANG="bg-BG" python scripts/recognize_local.py

```

### Language Examples

> For a list of languages, see: http://www.lingoes.net/en/translator/langcode.htm

```sh
python scripts/langs.py
#> -------------------
#> LANG: en-US
#> TRANSCRIPT: how old is the Brooklyn Bridge
#> CONFIDENCE: 0.987629
#> -------------------
#> LANG: es
#> TRANSCRIPT: a un niño
#> CONFIDENCE: 0.76107144
#> -------------------
#> LANG: jp
#> TRANSCRIPT: arigato
#> CONFIDENCE: 0.98762906
#> -------------------
#> LANG: fr
#> TRANSCRIPT: et c'est la dictée numéro 1
#> CONFIDENCE: 0.96079487
#> -------------------
#> LANG: bg-BG
#> TRANSCRIPT: Да станах днеска в 9 часа
#> CONFIDENCE: 0.7405557
#> -------------------
#> LANG: zh
#> TRANSCRIPT: 砸自己的脚
#> CONFIDENCE: 0.95644838
```
