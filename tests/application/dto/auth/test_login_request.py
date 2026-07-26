from src.application.dto.auth.login_request import LoginRequest


def test_should_create_login_request() -> None:
    request = LoginRequest(
        email="daniel@email.com",
        password="Senha123",
    )

    assert request.email == "daniel@email.com"
    assert request.password == "Senha123"