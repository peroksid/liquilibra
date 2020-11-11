from datetime import datetime

import pytest

from liquilibra import librasrv


@pytest.fixture
def client():
    librasrv.app.config['TESTING'] = True
    with librasrv.app.test_client() as client:
        yield client

def test_request_post(client):
    """Start with a blank database."""
    EMAIL='test@test.run'
    TITLE='This is the title'
    ID = '4242'
    NOW=datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    resp = client.post('/request', data=dict(
      email=EMAIL,
      title=TITLE,
      id=ID,
      timestamp=NOW
    ), follow_redirects=True)
    assert 200 == resp.status_code



def test_request_get(client):
    """Start with a blank database."""
    resp = client.get('/request')
    assert 405 == resp.status_code

