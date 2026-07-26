from datetime import datetime
from uuid import uuid4

from src.application.dto.auth.login_response import LoginResponse


def test_should_create_login_response() -> None:
    response = LoginResponse(
        id=uuid4(),
        name="Daniel",
        email="daniel@email.com",
        access_token="token-123",
        authenticated_at=datetime.now(),
    )

    assert response.name == "Daniel"
