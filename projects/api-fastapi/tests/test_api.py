from uuid import uuid4

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_contact():
    email = f"tatatest-{uuid4().hex}@example.com"

    response = client.post(
        "/contacts",
        json={"name": "Test User", "email": email},
    )

    assert response.status_code == 201
    created = response.json()
    assert created["email"] == email

    listing = client.get("/contacts")
    assert listing.status_code == 200
    assert any(item["email"] == email for item in listing.json())
