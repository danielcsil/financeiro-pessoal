from __future__ import annotations

from uuid import UUID

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.value_objects.email import Email


class InMemoryUserRepository(UserRepository):
    """
    In-memory implementation of UserRepository.

    Intended for unit tests and local development.
    """

    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def add(self, user: User) -> None:
        self._users[user.id] = user

    def remove(self, user: User) -> None:
        self._users.pop(user.id, None)

    def exists_by_id(self, user_id: UUID) -> bool:
        return user_id in self._users

    def find_by_id(self, user_id: UUID) -> User | None:
        return self._users.get(user_id)

    def find_by_email(self, email: Email) -> User | None:
        for user in self._users.values():
            if str(user.email) == str(email):
                return user

        return None

    def exists_by_email(self, email: Email) -> bool:
        return self.find_by_email(email) is not None

    def save(self, user: User) -> None:
        self.add(user)

    def update(self, user: User) -> None:
        self.add(user)

    def delete(self, user_id: UUID) -> None:
        self._users.pop(user_id, None)
