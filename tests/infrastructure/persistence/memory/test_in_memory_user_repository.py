from __future__ import annotations

from infrastructure.memory.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)

from src.domain.entities.user import User
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import HashedPassword

from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)


def test_should_find_user_by_email() -> None:

    repository = InMemoryUserRepository()

    hasher = BcryptPasswordHasher()

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=HashedPassword(
            hasher.hash("Senha123"),
        ),
    )

    repository.add(user)

    found = repository.find_by_email(
        Email("daniel@email.com"),
    )

    assert found is not None
    assert found.id == user.id
    assert found.email == user.email