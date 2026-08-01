from __future__ import annotations

"""
Financial Account Repository.

===============================================================================
Purpose
===============================================================================

Defines the persistence contract for FinancialAccount entities.

Repositories abstract the persistence mechanism used by the application,
allowing the Domain and Application layers to remain completely independent
from SQLAlchemy or any other database technology.

Concrete implementations are provided exclusively by the Infrastructure Layer.

===============================================================================
Responsibilities
===============================================================================

A FinancialAccountRepository is responsible for:

    • storing financial accounts;

    • retrieving financial accounts;

    • updating existing accounts;

    • removing accounts;

    • verifying business constraints that depend on persisted data.

Repositories must not implement business rules.

===============================================================================
Architecture
===============================================================================

Application Use Case

        │

        ▼

FinancialAccountRepository

        │

        ▼

SQLAlchemyFinancialAccountRepository

        │

        ▼

Database

===============================================================================
Design Principles
===============================================================================

• Works exclusively with Domain Entities.

• Never exposes ORM models.

• Never returns persistence-specific objects.

• Does not manage transactions. Transaction boundaries are coordinated by the
  Unit of Work.
"""

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from src.domain.entities.financial_account import FinancialAccount


class FinancialAccountRepository(ABC):
    """
    Defines the persistence contract for FinancialAccount entities.
    """

    @abstractmethod
    def add(
        self,
        account: FinancialAccount,
    ) -> None:
        """
        Persists a new financial account.
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        account: FinancialAccount,
    ) -> None:
        """
        Persists modifications performed on an existing financial account.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(
        self,
        account_id: UUID,
    ) -> FinancialAccount | None:
        """
        Retrieves a financial account by its unique identifier.

        Returns
        -------
        FinancialAccount | None
            The corresponding account, or None when it does not exist.
        """
        raise NotImplementedError

    @abstractmethod
    def find_all_by_user(
        self,
        user_id: UUID,
    ) -> list[FinancialAccount]:
        """
        Returns every financial account owned by a specific user.

        The ordering of the returned accounts is implementation-defined.
        """
        raise NotImplementedError

    @abstractmethod
    def exists_by_name(
        self,
        user_id: UUID,
        name: str,
    ) -> bool:
        """
        Checks whether a user already owns an account with the specified name.

        Returns
        -------
        bool
            True when an account with the same name already exists.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        account: FinancialAccount,
    ) -> None:
        """
        Removes a financial account.

        Concrete implementations may choose between physical deletion or
        logical deletion according to business requirements.
        """
        raise NotImplementedError