from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.domain.repositories.user_repository import (
    UserRepository,
)


class UnitOfWork(ABC):
    """
    Coordinates repositories inside a transaction.
    """

    users: UserRepository

    @abstractmethod
    def __enter__(self) -> "UnitOfWork":
        raise NotImplementedError

    @abstractmethod
    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError