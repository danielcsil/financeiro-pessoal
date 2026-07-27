from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_should_return_validation_error_when_email_is_missing():
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Daniel",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    assert response.status_code == 422

    body = response.json()

    assert body["error"] == "VALIDATION_ERROR"

    assert body["details"][0]["field"] == "email"

def test_should_return_validation_error_for_invalid_json():
    response = client.post(
        "/api/auth/login",
        data="{",
        headers={
            "Content-Type": "application/json",
        },
    )

    assert response.status_code == 422

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
