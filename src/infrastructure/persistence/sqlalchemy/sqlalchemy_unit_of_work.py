from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.domain.repositories.unit_of_work import UnitOfWork
from src.domain.repositories.user_repository import UserRepository

from src.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)


class SqlAlchemyUnitOfWork(UnitOfWork):
    """
    SQLAlchemy implementation of the Unit of Work pattern.

    A new database session is created for each use case execution.
    """

    def __init__(
        self,
        session_factory: sessionmaker[Session],
    ) -> None:
        self._session_factory = session_factory
        self._session: Session | None = None

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        self._session = self._session_factory()

        self.users = SqlAlchemyUserRepository(
            self._session,
        )

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        try:
            if exc is not None:
                self.rollback()
        finally:
            if self._session is not None:
                self._session.close()

            self._session = None

    def commit(self) -> None:
        """
        Commits the current transaction.
        """

        if self._session is None:
            raise RuntimeError(
                "UnitOfWork has not been started."
            )

        self._session.commit()

    def rollback(self) -> None:
        """
        Rolls back the current transaction.
        """

        if self._session is None:
            return

        self._session.rollback()