from __future__ import annotations

"""
Financial Account Mapper.

===============================================================================
Purpose
===============================================================================

Converts FinancialAccount objects between the Domain Layer and the
Infrastructure Layer.

The mapper is the only component responsible for translating:

    • Domain Entities into SQLAlchemy persistence models;

    • SQLAlchemy persistence models back into Domain Entities.

By centralizing these conversions, the Domain Layer remains completely
independent from SQLAlchemy and any persistence technology.

===============================================================================
Architecture
===============================================================================

                Domain Layer

                FinancialAccount
                        │
                        ▼
            FinancialAccountMapper
               ▲                ▼
               │                │
               │                ▼
      SQLAlchemy Model   Infrastructure Layer

===============================================================================
Responsibilities
===============================================================================

This mapper is responsible for:

    • converting domain entities into ORM models;

    • reconstructing domain entities from persisted records;

    • isolating persistence concerns from business logic.

The mapper must never:

    • implement business rules;

    • validate entities;

    • access the database.

===============================================================================
Design Principles
===============================================================================

• Stateless.

• Deterministic.

• Infrastructure concern only.

• Single Responsibility Principle.

• One-to-one mapping between Entity and Model.
"""

from typing import final

from src.domain.entities.financial_account import FinancialAccount
from src.infrastructure.database.models.financial_account_model import (
    FinancialAccountModel,
)


@final
class FinancialAccountMapper:
    """
    Converts FinancialAccount objects between the Domain and Infrastructure
    layers.

    Every conversion preserves the complete state of the financial account
    without introducing business behavior.
    """

    @staticmethod
    def to_model(
        account: FinancialAccount,
    ) -> FinancialAccountModel:
        """
        Converts a domain entity into its SQLAlchemy persistence model.

        Parameters
        ----------
        account:
            Domain entity to be persisted.

        Returns
        -------
        FinancialAccountModel

            SQLAlchemy model representing the same financial account.
        """

        return FinancialAccountModel(
            id=account.id,
            user_id=account.user_id,
            name=account.name,
            institution=account.institution,
            account_type=account.account_type,
            initial_balance=account.initial_balance,
            current_balance=account.current_balance,
            color=account.color,
            icon=account.icon,
            include_in_cash_flow=account.include_in_cash_flow,
            include_in_net_worth=account.include_in_net_worth,
            active=account.active,
            created_at=account.created_at,
            updated_at=account.updated_at,
        )

    @staticmethod
    def to_entity(
        model: FinancialAccountModel,
    ) -> FinancialAccount:
        """
        Reconstructs a domain entity from its persistence model.

        Parameters
        ----------
        model:
            SQLAlchemy model loaded from the database.

        Returns
        -------
        FinancialAccount

            Domain entity reconstructed from persisted data.
        """

        return FinancialAccount(
            id=model.id,
            user_id=model.user_id,
            name=model.name,
            institution=model.institution,
            account_type=model.account_type,
            initial_balance=model.initial_balance,
            current_balance=model.current_balance,
            color=model.color,
            icon=model.icon,
            include_in_cash_flow=model.include_in_cash_flow,
            include_in_net_worth=model.include_in_net_worth,
            active=model.active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )