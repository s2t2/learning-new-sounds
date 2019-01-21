# Contributor's Guide

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Download or clone from GitHub source:

```sh
git clone https://github.com/s2t2/learning-new-sounds.git # or git@github.com:s2t2/learning-new-sounds.git
```

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
pip install --upgrade google-cloud-speech
pip install python-dotenv
pip install pyaudio # on Mac OS, first run: `brew install portaudio` (see http://people.csail.mit.edu/hubert/pyaudio/#downloads)
pip install SpeechRecognition # depends on pyaudio
```

## Authorization

Setup a new project in the [Google API Console](https://console.cloud.google.com/cloud-resource-manager), enable the "Cloud Speech API" for this project, and download the corresponding credentials .json file into the "credentials" directory of this repository. Note the full path to this credentials file.

Create a new `.env` file in the root directory of this repository, as a copy of the `env.example` file, and update the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in the new `.env` file to point to the credentials .json filepath.

## Usage

Recognize speech:

```sh
python recognize.py
```

> NOTE: right now this is using a hard-coded audio file and recognition word
