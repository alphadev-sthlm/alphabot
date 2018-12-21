import os
import re
import tempfile

import pytest

from alphabot import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def root(client):
    return client.get('/')


def alphabot(client, data):
    return client.post('/alphabot', data=dict(
        text=data
    ), follow_redirects=True)


def test_root(client):
    """Make sure / is callable."""

    rv = root(client)
    assert b'Alphabot running in development' in rv.data


def test_alphabot_help(client):
    """Test post alphabot without arguments"""

    rv = alphabot(client, '')
    assert b'List all commands' in rv.data


def test_alphabot_eko(client):
    """Test eko a word"""

    rv = alphabot(client, 'eko hej')
    assert b'in_channel' in rv.data
    assert b'"text": "hej"' in rv.data


def test_alphabot_celebrate(client):
    """Test post"""

    rv = alphabot(client, 'celebrate')
    regex = re.compile('.*":[a-z_]+:".*')  # some emoji
    assert regex.match(str(rv.data))
