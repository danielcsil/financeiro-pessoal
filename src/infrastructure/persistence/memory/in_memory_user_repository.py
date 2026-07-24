from __future__ import annotations

from uuid import UUID

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    """
    In-memory implementation of UserRepository.

    Intended for unit tests and local development.
    """

    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def save(self, user: User) -> None:
        self._users[user.id] = user

    def update(self, user: User) -> None:
        if user.id not in self._users:
            raise KeyError(f"User '{user.id}' not found.")

        self._users[user.id] = user

    def delete(self, user_id: UUID) -> None:
        self._users.pop(user_id, None)

    def find_by_id(self, user_id: UUID) -> User | None:
        return self._users.get(user_id)

    def find_by_email(self, email: str) -> User | None:
        normalized_email = email.strip().lower()

        for user in self._users.values():
            if user.email == normalized_email:
                return user

        return None

    def exists_by_email(self, email: str) -> bool:
        return self.find_by_email(email) is not None