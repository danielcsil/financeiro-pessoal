from __future__ import annotations

from uuid import uuid4

import pytest

from infrastructure.memory.in_memory_unit_of_work import (
    InMemoryUnitOfWork,
)

from src.application.use_cases.auth.get_current_user import (
    GetCurrentUserUseCase,
)
from src.domain.entities.user import User
from src.domain.exceptions import InvalidCredentialsError
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import (
    HashedPassword,
)
from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)


def test_should_return_current_user() -> None:
    """
    Should return the authenticated user.
    """

    uow = InMemoryUnitOfWork()

    hasher = BcryptPasswordHasher()

    user = User.create(
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

    use_case = GetCurrentUserUseCase(
        unit_of_work=uow,
    )

    response = use_case.execute(
        user.id,
    )

    assert response.id == user.id
    assert response.email == "daniel@email.com"
    assert response.name == "Daniel"


def test_should_raise_error_when_user_not_found() -> None:
    """
    Should raise InvalidCredentialsError when the user does not exist.
    """

    use_case = GetCurrentUserUseCase(
        unit_of_work=InMemoryUnitOfWork(),
    )

    with pytest.raises(
        InvalidCredentialsError,
    ):
        use_case.execute(
            uuid4(),
        )