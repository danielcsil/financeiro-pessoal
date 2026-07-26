from uuid import uuid4

import pytest

from src.application.use_cases.auth.get_current_user import (
    GetCurrentUserUseCase,
)
from src.domain.entities.user import User
from src.domain.exceptions import InvalidCredentialsError
from src.infrastructure.persistence.memory.in_memory_user_repository import (
    InMemoryUserRepository,
)


def test_should_return_current_user() -> None:
    repository = InMemoryUserRepository()

    user = User.create(
        name="Daniel",
        email="daniel@email.com",
        password="..."
    )

    repository.save(user)

    use_case = GetCurrentUserUseCase(repository)

    response = use_case.execute(user.id)

    assert response.id == user.id
    assert response.email == "daniel@email.com"


def test_should_raise_error_when_user_not_found() -> None:
    repository = InMemoryUserRepository()

    use_case = GetCurrentUserUseCase(repository)

    with pytest.raises(InvalidCredentialsError):
        use_case.execute(uuid4())