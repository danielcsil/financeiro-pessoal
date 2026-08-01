from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.domain.repositories.financial_account_repository import (
    FinancialAccountRepository,
)
from src.domain.repositories.user_repository import (
    UserRepository,
)


class UnitOfWork(ABC):
    """
    Defines the transactional boundary of the application.

    ============================================================================
    Purpose
    ============================================================================

    The Unit of Work coordinates one or more repositories during the execution
    of a business operation.

    Instead of allowing repositories to independently persist changes, the
    application layer delegates transaction management to the Unit of Work.

    This ensures that all modifications performed during a use case are
    committed or rolled back as a single atomic transaction.

    ============================================================================
    Why is this important?
    ============================================================================

    Consider a future business operation such as:

        Create Financial Account

            ↓

        Register Opening Balance

            ↓

        Write Audit Log

            ↓

        Publish Domain Event

    Every step above belongs to the same business transaction.

    If any operation fails, all previous modifications must be reverted.

    The Unit of Work guarantees this consistency.

    ============================================================================
    Repository Coordination
    ============================================================================

    The Unit of Work acts as a gateway to the repositories required by the
    application layer.

    Each repository represents a different aggregate root.

    Current repositories:

        • Users
        • Financial Accounts

    Future modules will naturally extend this contract with repositories for:

        • Credit Cards
        • Transactions
        • Investments
        • Financial Goals
        • Loans
        • Budgets

    ============================================================================
    Context Manager
    ============================================================================

    Concrete implementations should support Python's context manager protocol.

    Example:

        with unit_of_work:

            ...

            unit_of_work.commit()

    If commit() is never executed, the implementation should rollback the
    transaction automatically.
    """

    users: UserRepository

    financial_accounts: FinancialAccountRepository

    @abstractmethod
    def __enter__(self) -> "UnitOfWork":
        """
        Opens a transactional context.

        Returns
        -------
        UnitOfWork
            The active transactional context.
        """
        raise NotImplementedError

    @abstractmethod
    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        """
        Closes the transactional context.

        Implementations should automatically rollback the transaction whenever
        an exception propagates outside the context manager.
        """
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        """
        Persists every modification performed during the current transaction.

        After a successful commit, all tracked changes become permanent.
        """
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        """
        Reverts every modification performed during the current transaction.

        This method restores the persistence context to the state that existed
        before the transaction started.
        """
        raise NotImplementedError