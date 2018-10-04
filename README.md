# alphabot [![Build Status](https://travis-ci.org/alphadev-sthlm/alphabot.svg?branch=master)](https://travis-ci.org/alphadev-sthlm/alphabot)
Our slackbot

## Setup

Get pip

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py

Get virtualenv

    sudo pip install virtualenv
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

Create .env file and insert SLACK_TOKEN found https://api.slack.com/apps under Basic Information for app. 

    cp .env.example .env

Run locally

    python alphabot.py
    
Run tests

    python -m pytest tests

Deploy (will create lambda with -dev suffix)

    zappa deploy
    zappa update
    zappa tail

## Common problems

If you get inexplicable zappa error 

    ImportError: bad magic number in 'config': b'\x03\xf3\r\n'

Solution

    find . -name \*.pyc -delete
