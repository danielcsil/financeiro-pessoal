from __future__ import annotations

"""
SQLAlchemy Financial Account Repository.

===============================================================================
Purpose
===============================================================================

Provides the SQLAlchemy implementation of the FinancialAccountRepository
interface.

This repository is responsible for translating operations on Domain Entities
into persistence operations performed by SQLAlchemy.

The Application Layer interacts exclusively with the repository interface,
remaining completely unaware of the underlying persistence technology.

===============================================================================
Responsibilities
===============================================================================

This repository is responsible for:

    • persisting new financial accounts;

    • updating existing financial accounts;

    • retrieving financial accounts;

    • checking business constraints that depend on persisted data;

    • performing logical deletion.

The repository does not implement business rules. Its responsibility is
restricted to persistence concerns.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

FinancialAccountRepository

        │

        ▼

SqlAlchemyFinancialAccountRepository

        │

        ▼

FinancialAccountMapper

        │

        ▼

FinancialAccountModel

        │

        ▼

Database

===============================================================================
Transactions
===============================================================================

Repositories never commit or rollback transactions.

Transaction boundaries are coordinated exclusively by the UnitOfWork.
"""

from typing import final
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.financial_account import FinancialAccount
from src.domain.repositories.financial_account_repository import (
    FinancialAccountRepository,
)
from src.infrastructure.database.mappers.financial_account_mapper import (
    FinancialAccountMapper,
)
from src.infrastructure.database.models.financial_account_model import (
    FinancialAccountModel,
)


@final
class SqlAlchemyFinancialAccountRepository(
    FinancialAccountRepository,
):
    """
    SQLAlchemy implementation of FinancialAccountRepository.

    This class encapsulates every persistence operation related to
    FinancialAccount entities while keeping the Domain Layer completely
    independent from SQLAlchemy.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        """
        Initializes the repository.

        Parameters
        ----------
        session:
            SQLAlchemy session associated with the current UnitOfWork.
        """

        self._session = session

    def add(
        self,
        account: FinancialAccount,
    ) -> None:
        """
        Persists a new financial account.

        The entity is converted into its ORM representation before being added
        to the current persistence context.

        The transaction is not committed here.
        """

        model = FinancialAccountMapper.to_model(
            account,
        )

        self._session.add(
            model,
        )

    def update(
        self,
        account: FinancialAccount,
    ) -> None:
        """
        Synchronizes the current state of a financial account with the database.

        SQLAlchemy's merge operation is used because the entity originates from
        the Domain Layer and may not be attached to the current session.

        The transaction is not committed here.
        """

        model = FinancialAccountMapper.to_model(
            account,
        )

        self._session.merge(
            model,
        )

    def find_by_id(
        self,
        account_id: UUID,
    ) -> FinancialAccount | None:
        """
        Retrieves a financial account by its unique identifier.

        Parameters
        ----------
        account_id:
            Identifier of the requested financial account.

        Returns
        -------
        FinancialAccount | None

            The corresponding domain entity or None when the account does not
            exist.
        """

        statement = (
            select(
                FinancialAccountModel,
            )
            .where(
                FinancialAccountModel.id == account_id,
            )
        )

        model = self._session.scalar(
            statement,
        )

        if model is None:
            return None

        return FinancialAccountMapper.to_entity(
            model,
        )

    def find_all_by_user(
        self,
        user_id: UUID,
    ) -> list[FinancialAccount]:
        """
        Retrieves every active financial account belonging to a user.

        Results are ordered alphabetically by account name.

        Parameters
        ----------
        user_id:
            Identifier of the account owner.

        Returns
        -------
        list[FinancialAccount]

            Active financial accounts owned by the specified user.
        """

        statement = (
            select(
                FinancialAccountModel,
            )
            .where(
                FinancialAccountModel.user_id == user_id,
            )
            .where(
                FinancialAccountModel.active.is_(True),
            )
            .order_by(
                FinancialAccountModel.name,
            )
        )

        models = self._session.scalars(
            statement,
        ).all()

        return [
            FinancialAccountMapper.to_entity(
                model,
            )
            for model in models
        ]

    def exists_by_name(
        self,
        user_id: UUID,
        name: str,
    ) -> bool:
        """
        Checks whether an active financial account with the specified name
        already exists for a given user.

        Parameters
        ----------
        user_id:
            Owner identifier.

        name:
            Financial account name.

        Returns
        -------
        bool

            True when an account with the same name already exists.
        """

        statement = (
            select(
                FinancialAccountModel.id,
            )
            .where(
                FinancialAccountModel.user_id == user_id,
            )
            .where(
                FinancialAccountModel.name == name,
            )
            .where(
                FinancialAccountModel.active.is_(True),
            )
        )

        return (
            self._session.scalar(
                statement,
            )
            is not None
        )

    def remove(
        self,
        account: FinancialAccount,
    ) -> None:
        """
        Performs a logical deletion of a financial account.

        Instead of removing the database record, the account is marked as
        inactive. This preserves the complete financial history while preventing
        the account from appearing in normal queries.

        If the account no longer exists, the operation silently returns.
        """

        model = self._session.get(
            FinancialAccountModel,
            account.id,
        )

        if model is None:
            return

        model.active = False