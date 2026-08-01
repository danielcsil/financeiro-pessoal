from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_should_register_user() -> None:
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Daniel"
    assert body["email"] == "daniel@email.com"
    assert "id" in body

def test_should_return_409_when_email_already_exists():
    client.post(
        "/api/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    response = client.post(
        "/api/auth/register",
        json={
            "name": "Outro",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    assert response.status_code == 409

    body = response.json()

    assert body["error"] == "EMAIL_ALREADY_EXISTS"

def test_should_return_400_when_passwords_do_not_match():
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "87654321",
            "accept_terms": True,
        },
    )

    assert response.status_code == 400

    body = response.json()

    assert body["error"] == "PASSWORD_MISMATCH"

def test_should_return_400_when_terms_are_not_accepted():
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": False,
        },
    )

    assert response.status_code == 400

    body = response.json()

    assert body["error"] == "TERMS_NOT_ACCEPTED"
