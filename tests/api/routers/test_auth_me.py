from fastapi.testclient import TestClient


def test_me_without_token_returns_401(
    client: TestClient,
) -> None:
    response = client.get("/auth/me")

    assert response.status_code == 401

def test_me_with_invalid_token_returns_401(
    client: TestClient,
) -> None:
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid-token",
        },
    )

    assert response.status_code == 401