import pytest
from fastapi.testclient import TestClient
from sqlalchemy import delete

from src.api.main import app
from src.api.dependencies.repositories import get_user_repository
from src.infrastructure.database.session_factory import SessionFactory
from src.infrastructure.persistence.sqlalchemy.models.user_model import (
    UserModel,
)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_auth_state():
    get_user_repository.cache_clear()

    with SessionFactory() as session:
        session.execute(delete(UserModel))
        session.commit()

    yield

    get_user_repository.cache_clear()


def register_user(
    client: TestClient,
    *,
    name: str = "Daniel",
    email: str = "daniel@email.com",
    password: str = "12345678",
):
    return client.post(
        "/api/auth/register",
        json={
            "name": name,
            "email": email,
            "password": password,
            "password_confirmation": password,
            "accept_terms": True,
        },
    )
