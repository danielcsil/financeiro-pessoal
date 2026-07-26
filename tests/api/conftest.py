import pytest
from fastapi.testclient import TestClient

from src.api.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

def register_user(
    client: TestClient,
    *,
    name: str = "Daniel",
    email: str = "daniel@email.com",
    password: str = "12345678",
):
    return client.post(
        "/auth/register",
        json={
            "name": name,
            "email": email,
            "password": password,
            "password_confirmation": password,
            "accept_terms": True,
        },
    )