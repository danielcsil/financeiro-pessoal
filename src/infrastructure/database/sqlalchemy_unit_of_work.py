from __future__ import annotations

"""
SQLAlchemy Unit of Work.

===============================================================================
Purpose
===============================================================================

Coordinates a complete transactional boundary using SQLAlchemy.

The Unit of Work is responsible for:

    • opening a database session;

    • creating repository instances;

    • coordinating commits;

    • coordinating rollbacks;

    • closing database resources.

Application use cases should never manipulate SQLAlchemy sessions directly.
Instead, they interact only with repositories exposed by this class.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

UnitOfWork (Domain Contract)

        │

        ▼

SqlAlchemyUnitOfWork

        │

        ▼

SQLAlchemy Session

        │

        ▼

Repositories

        │

        ▼

Database

===============================================================================
Transaction Lifecycle
===============================================================================

with UnitOfWork() as uow

    ├── open session

    ├── execute repositories

    ├── commit()

    └── close session

If an exception occurs, rollback() is automatically executed before the session
is closed.

===============================================================================
Design Principles
===============================================================================

• One UnitOfWork per application use case.

• One SQLAlchemy Session per UnitOfWork.

• Repository lifetime equals transaction lifetime.

• Infrastructure concern only.
"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.domain.repositories.unit_of_work import UnitOfWork

from src.infrastructure.database.repositories.sqlalchemy_financial_account_repository import (
    SqlAlchemyFinancialAccountRepository,
)
from src.infrastructure.database.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)


class SqlAlchemyUnitOfWork(UnitOfWork):
    """
    SQLAlchemy implementation of the UnitOfWork abstraction.

    This class manages the complete transactional lifecycle for an application
    request.
    """

    def __init__(
        self,
        session_factory: sessionmaker[Session],
    ) -> None:
        """
        Parameters
        ----------
        session_factory:
            Factory responsible for creating SQLAlchemy sessions.
        """

        self._session_factory = session_factory
        self._session: Session | None = None

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        """
        Opens a new transactional scope.

        Repository instances are created using the same SQLAlchemy session,
        ensuring that every persistence operation participates in the same
        transaction.
        """

        self._session = self._session_factory()

        self.users = SqlAlchemyUserRepository(
            self._session,
        )

        self.financial_accounts = (
            SqlAlchemyFinancialAccountRepository(
                self._session,
            )
        )

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        """
        Finalizes the transactional scope.

        If an exception escaped the use case, the transaction is rolled back.
        Regardless of the outcome, the database session is always closed.
        """

        try:
            if exc_type is not None:
                self.rollback()
        finally:
            if self._session is not None:
                self._session.close()

    def commit(
        self,
    ) -> None:
        """
        Commits the current transaction.
        """

        assert self._session is not None

        self._session.commit()

    def rollback(
        self,
    ) -> None:
        """
        Rolls back the current transaction.
        """

        assert self._session is not None

        self._session.rollback()