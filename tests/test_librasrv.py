from datetime import datetime

import pytest

from liquilibra import librasrv


@pytest.fixture
def client():
    librasrv.app.config["TESTING"] = True
    with librasrv.app.test_client() as client:
        yield client


def test_request_post(client):
    """Roughly check the endpoint is in place."""
    EMAIL = "test@test.run"
    TITLE = "This is the title"
    ID = "4242"
    NOW = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    resp = client.post(
        "/request",
        data=dict(email=EMAIL, title=TITLE, id=ID, timestamp=NOW),
        follow_redirects=True,
    )
    assert resp.is_json
    assert 200 == resp.status_code


def test_request_get_collection(client):
    """TODO: Add check other methods bounced away as well"""
    expected_json = {
        "email": "test@test.run",
        "id": "4242",
        "title": "This is the title",
    }
    expected_json.update({"timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    resp = client.get("/request", follow_redirects=True)
    assert 200 == resp.status_code
    assert resp.is_json
    assert resp.json == {"requests": [expected_json]}


def test_request_get(client):
    """TODO: Add check other methods bounced away as well"""
    resp = client.get("/request/4242")
    expected_json = {
        "email": "test@test.run",
        "id": "4242",
        "title": "This is the title",
    }
    expected_json.update({"timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    assert resp.json == expected_json
    assert resp.is_json
    assert 200 == resp.status_code

def test_request_delete(client):
  # TODO: 404 for missing ID
  resp = client.delete("/request/4242")
  assert 200 == resp.status_code
  assert not resp.is_json
  assert b'' == resp.data