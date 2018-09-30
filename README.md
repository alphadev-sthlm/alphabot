# alphabot
Our slackbot

## Setup

Get pip

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py

Get virtualenv

    sudo pip install virtualenv
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt


Create .env file

    SLACK_API_TOKEN=XXXX
    APP_ENV=development

Run locally

    python alphabot.py

Deploy (will create lambda with -dev suffix)

    zappa deploy
    zappa update
    zappa tail

## Common problems

If you get inexplicable zappa error 

    ImportError: bad magic number in 'config': b'\x03\xf3\r\n'

Solution

    find . -name \*.pyc -delete