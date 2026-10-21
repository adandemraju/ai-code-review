from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_webhook_opened():
    response = client.post(
        "/webhooks/github",
        json={"action" : "opened" }
    )
    assert response.status_code == 200
    assert response.json() == {
        "should_review": True
    }

def test_post_webhook_synch():
    response = client.post(
        "/webhooks/github",
        json={"action" : "synchronize" }
    )
    assert response.status_code == 200
    assert response.json() == {
        "should_review": True
    }   

def test_post_webhook_reopened():
    response = client.post(
        "/webhooks/github",
        json={"action" : "reopened" }
    )
    assert response.status_code == 200
    assert response.json() == {
        "should_review": True
    }

def test_post_webhook_closed():
    response = client.post(
        "/webhooks/github",
        json={"action" : "closed" }
    )
    assert response.status_code == 200
    assert response.json() == {
        "should_review": False
    }

def test_post_webhook_unknown():
    response = client.post(
        "/webhooks/github",
        json={"action" : "unknown_action" }
    )
    assert response.status_code == 200
    assert response.json() == {
        "should_review": False
    }