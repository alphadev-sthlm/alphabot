import os
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


def slash(client, data):
    return client.post('/slash', data=dict(
        test='test'
    ), follow_redirects=True)


def test_root(client):
    """Make sure / is callable."""

    rv = root(client)
    assert b'Alphabot running in development' in rv.data


def test_slash(client):
    """Test post"""

    rv = slash(client, 'asx')
    assert b'in_channel' in rv.data
    assert b'Test response successful!' in rv.data
