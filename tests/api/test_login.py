from fastapi.testclient import TestClient

def test_should_login_user(
    client: TestClient,
) -> None:
    client.post(
        "/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "daniel@email.com",
            "password": "12345678",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "Daniel"
    assert body["email"] == "daniel@email.com"
    assert isinstance(body["access_token"], str)

def test_should_return_401_when_user_does_not_exist(
    client: TestClient,
) -> None:
    response = client.post(
        "/auth/login",
        json={
            "email": "naoexiste@email.com",
            "password": "12345678",
        },
    )

    assert response.status_code == 401

    assert response.json()["error"] == "INVALID_CREDENTIALS"

def test_should_return_401_when_password_is_invalid(
    client: TestClient,
) -> None:

    client.post(
        "/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "daniel@email.com",
            "password": "senha_errada",
        },
    )

    assert response.status_code == 401

    assert response.json()["error"] == "INVALID_CREDENTIALS"

def test_me_with_valid_token_returns_current_user(
    client: TestClient,
) -> None:
    client.post(
        "/auth/register",
        json={
            "name": "Daniel",
            "email": "daniel@email.com",
            "password": "12345678",
            "password_confirmation": "12345678",
            "accept_terms": True,
        },
    )

    login_response = client.post(
        "/auth/login",
        json={
            "email": "daniel@email.com",
            "password": "12345678",
        },
    )

    access_token = login_response.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "Daniel"
    assert body["email"] == "daniel@email.com"