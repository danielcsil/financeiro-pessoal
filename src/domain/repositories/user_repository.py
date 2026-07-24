from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user import User


class UserRepository(ABC):
    """
    Defines the contract for user persistence.

    Application use cases depend on this abstraction instead of
    concrete database implementations.
    """

    @abstractmethod
    def save(self, user: User) -> None:
        """
        Persists a new user.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> None:
        """
        Updates an existing user.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        """
        Deletes a user by its identifier.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, user_id: UUID) -> User | None:
        """
        Returns a user by its identifier.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """
        Returns a user by e-mail.
        """
        raise NotImplementedError

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        """
        Checks whether a user with the given e-mail already exists.
        """
        raise NotImplementedError