from __future__ import annotations

import pytest

from src.application.dto.auth.login_request import LoginRequest
from src.application.use_cases.auth.login_user import LoginUserUseCase
from src.domain.entities.user import User
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import HashedPassword
from src.infrastructure.persistence.memory.in_memory_user_repository import (
    InMemoryUserRepository,
)
from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)
from src.infrastructure.security.bcrypt_password_verifier import (
    BcryptPasswordVerifier,
)
from src.infrastructure.security.fake_token_provider import FakeTokenProvider


def create_use_case() -> LoginUserUseCase:
    return LoginUserUseCase(
        user_repository=InMemoryUserRepository(),
        password_verifier=BcryptPasswordVerifier(),
        token_provider=FakeTokenProvider(),
    )


def test_should_raise_error_when_user_does_not_exist() -> None:
    use_case = create_use_case()

    with pytest.raises(InvalidCredentialsError):
        use_case.execute(
            LoginRequest(
                email="daniel@email.com",
                password="Senha123",
            )
        )




def test_should_raise_error_when_password_is_invalid() -> None:
    repository = InMemoryUserRepository()
    hasher = BcryptPasswordHasher()

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=HashedPassword(
            hasher.hash("Senha123")
        ),
    )

    repository.save(user)

    use_case = LoginUserUseCase(
        user_repository=repository,
        password_verifier=BcryptPasswordVerifier(),
        token_provider=FakeTokenProvider(),
    )

    with pytest.raises(InvalidCredentialsError):
        use_case.execute(
            LoginRequest(
                email="daniel@email.com",
                password="SenhaErrada",
            )
        )

def test_should_login_successfully() -> None:
    repository = InMemoryUserRepository()
    hasher = BcryptPasswordHasher()

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=HashedPassword(
            hasher.hash("Senha123")
        ),
    )

    repository.save(user)

    use_case = LoginUserUseCase(
        user_repository=repository,
        password_verifier=BcryptPasswordVerifier(),
        token_provider=FakeTokenProvider(),
    )

    response = use_case.execute(
        LoginRequest(
            email="daniel@email.com",
            password="Senha123",
        )
    )

    assert response.id == user.id
    assert response.name == user.name
    assert response.email == str(user.email)
    assert response.authenticated_at is not None
    assert response.access_token == f"token-{user.id}"
