from __future__ import annotations

"""
In-Memory Unit of Work.

===============================================================================
Purpose
===============================================================================

Provides an in-memory implementation of the UnitOfWork abstraction for unit
tests.

This implementation reproduces the same behavior expected from the production
SqlAlchemyUnitOfWork without requiring a database connection.

Repositories remain alive during the lifetime of the Unit of Work, allowing
multiple operations to participate in the same logical transaction.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

UnitOfWork

        │

        ▼

InMemoryUnitOfWork

        │

        ├───────────────┐
        ▼               ▼

InMemoryUserRepository
InMemoryFinancialAccountRepository

===============================================================================
Transaction Behavior
===============================================================================

Since everything is stored in memory, commit() and rollback() perform no
operations.

They exist only to preserve the same public contract used by the production
implementation.

This allows every use case to be tested exactly as it executes in production.

===============================================================================
Typical Usage
===============================================================================

uow = InMemoryUnitOfWork()

use_case = RegisterUserUseCase(
    unit_of_work=uow,
    password_hasher=BcryptPasswordHasher(),
)

response = use_case.execute(request)
"""

from infrastructure.memory.repositories.in_memory_financial_account_repository import (
    InMemoryFinancialAccountRepository,
)
from infrastructure.memory.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from src.domain.repositories.unit_of_work import UnitOfWork


class InMemoryUnitOfWork(UnitOfWork):
    """
    In-memory implementation of UnitOfWork.

    Intended exclusively for unit tests.
    """

    def __init__(self) -> None:
        self.users = InMemoryUserRepository()
        self.financial_accounts = (
            InMemoryFinancialAccountRepository()
        )

    def __enter__(self) -> "InMemoryUnitOfWork":
        """
        Opens a transactional context.

        Since repositories are already in memory, there is nothing to
        initialize.
        """
        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        """
        Finalizes the transactional context.

        If an exception occurred, rollback() is invoked to preserve the
        production contract.
        """

        if exc_type is not None:
            self.rollback()

    def commit(self) -> None:
        """
        Persists the current transaction.

        No action is required for the in-memory implementation.
        """
        return None

    def rollback(self) -> None:
        """
        Rolls back the current transaction.

        No action is required for the in-memory implementation.
        """
        return None