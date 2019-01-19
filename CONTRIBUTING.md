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

Create a new virtual environment:

```sh
conda create -n learning-sounds-env
```

Install package dependencies:

```sh
pip install --upgrade google-cloud-speech
pip install python-dotenv
```

## Usage

Recognize speech:

```sh
python recognize.py
```
