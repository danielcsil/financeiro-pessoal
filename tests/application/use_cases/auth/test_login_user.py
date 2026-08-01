from __future__ import annotations

import pytest

from infrastructure.memory.in_memory_unit_of_work import (
    InMemoryUnitOfWork,
)

from src.application.dto.auth.login_request import (
    LoginRequest,
)
from src.application.use_cases.auth.login_user import (
    LoginUserUseCase,
)
from src.domain.entities.user import User
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import (
    HashedPassword,
)
from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)
from src.infrastructure.security.bcrypt_password_verifier import (
    BcryptPasswordVerifier,
)
from src.infrastructure.security.fake_token_provider import (
    FakeTokenProvider,
)


def create_use_case() -> LoginUserUseCase:
    """
    Creates a LoginUserUseCase backed by an in-memory Unit of Work.
    """

    return LoginUserUseCase(
        unit_of_work=InMemoryUnitOfWork(),
        password_verifier=BcryptPasswordVerifier(),
        token_provider=FakeTokenProvider(),
    )


def test_should_raise_error_when_user_does_not_exist() -> None:
    """
    Should reject authentication when the user does not exist.
    """

    use_case = create_use_case()

    with pytest.raises(
        InvalidCredentialsError,
    ):
        use_case.execute(
            LoginRequest(
                email="daniel@email.com",
                password="Senha123",
            ),
        )


def test_should_raise_error_when_password_is_invalid() -> None:
    """
    Should reject authentication when the password is invalid.
    """

    uow = InMemoryUnitOfWork()

    hasher = BcryptPasswordHasher()

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=HashedPassword(
            hasher.hash(
                "Senha123",
            ),
        ),
    )

    uow.users.add(
        user,
    )

    use_case = LoginUserUseCase(
        unit_of_work=uow,
        password_verifier=BcryptPasswordVerifier(),
        token_provider=FakeTokenProvider(),
    )

    with pytest.raises(
        InvalidCredentialsError,
    ):
        use_case.execute(
            LoginRequest(
                email="daniel@email.com",
                password="SenhaErrada",
            ),
        )


def test_should_login_successfully() -> None:
    """
    Should authenticate a valid user.
    """

    uow = InMemoryUnitOfWork()

    hasher = BcryptPasswordHasher()

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=HashedPassword(
            hasher.hash(
                "Senha123",
            ),
        ),
    )

    uow.users.add(
        user,
    )

    use_case = LoginUserUseCase(
        unit_of_work=uow,
        password_verifier=BcryptPasswordVerifier(),
        token_provider=FakeTokenProvider(),
    )

    response = use_case.execute(
        LoginRequest(
            email="daniel@email.com",
            password="Senha123",
        ),
    )

    assert response.id == user.id
    assert response.name == user.name
    assert response.email == str(user.email)
    assert response.authenticated_at is not None
    assert response.access_token == f"token-{user.id}"