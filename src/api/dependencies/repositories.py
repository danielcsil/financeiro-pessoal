from __future__ import annotations

"""
Infrastructure dependency providers.

===============================================================================
Purpose
===============================================================================

This module centralizes the creation of infrastructure components required by
the Presentation and Application layers.

Its primary responsibility is exposing reusable infrastructure services such
as SQLAlchemy sessions and repository implementations.

Most modern Application Use Cases should obtain repositories through the
Unit of Work abstraction instead of depending directly on these providers.

These functions remain useful for:

    • legacy use cases;

    • integration tests;

    • standalone scripts;

    • migrations;

    • future maintenance tasks.

===============================================================================
Architecture
===============================================================================

                FastAPI

                   │

                   ▼

        Dependency Provider (this file)

                   │

        ┌──────────┴──────────┐
        ▼                     ▼

   SessionFactory        Repository

        │                     │

        └──────────┬──────────┘
                   ▼

             SQLAlchemy

===============================================================================
Notes
===============================================================================

The SessionFactory is shared by the entire application.

Each repository receives an independent SQLAlchemy Session.

Business operations should preferably be executed through the UnitOfWork,
which coordinates transactions and repository lifecycles.
"""

from functools import lru_cache

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.domain.repositories.financial_account_repository import (
    FinancialAccountRepository,
)
from src.domain.repositories.user_repository import (
    UserRepository,
)
from src.infrastructure.database.repositories.sqlalchemy_financial_account_repository import (
    SqlAlchemyFinancialAccountRepository,
)
from src.infrastructure.database.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)
from src.infrastructure.database.session_factory import (
    SessionFactory,
)


# ============================================================================
# Session
# ============================================================================


def get_session_factory() -> sessionmaker[Session]:
    """
    Returns the application's SQLAlchemy SessionFactory.

    The SessionFactory is configured once during application startup and reused
    throughout the application's lifetime.

    Returns
    -------
    sessionmaker[Session]
        SQLAlchemy Session factory.
    """

    return SessionFactory


def get_session() -> Session:
    """
    Creates a new SQLAlchemy Session.

    This helper is intended primarily for:

        • scripts;

        • tests;

        • maintenance tools.

    Business use cases should instead receive a UnitOfWork, which manages the
    session lifecycle and transaction boundaries.
    """

    return SessionFactory()


# ============================================================================
# Repositories
# ============================================================================


@lru_cache
def get_user_repository() -> UserRepository:
    """
    Returns a SQLAlchemy implementation of UserRepository.

    This provider exists mainly for backward compatibility.

    New Application Use Cases should obtain repositories through the
    UnitOfWork abstraction instead of accessing repositories directly.
    """

    return SqlAlchemyUserRepository(
        session=get_session(),
    )


@lru_cache
def get_financial_account_repository(
) -> FinancialAccountRepository:
    """
    Returns a SQLAlchemy implementation of FinancialAccountRepository.

    This provider exists mainly for:

        • integration tests;

        • standalone scripts;

        • temporary backward compatibility.

    The preferred approach for new code is obtaining repositories from the
    UnitOfWork.
    """

    return SqlAlchemyFinancialAccountRepository(
        session=get_session(),
    )