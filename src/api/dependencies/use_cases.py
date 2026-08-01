from __future__ import annotations

"""
Dependency providers for Application Use Cases.

===============================================================================
Purpose
===============================================================================

This module centralizes the construction of every Application Use Case exposed
by the REST API.

Instead of instantiating Use Cases directly inside the routers, FastAPI
delegates their creation to these provider functions.

This keeps the Presentation Layer focused exclusively on HTTP concerns while
the composition of the application remains centralized in a single location.

===============================================================================
Dependency Graph
===============================================================================

                HTTP Request
                      │
                      ▼
             FastAPI Dependency
                      │
                      ▼
            Use Case Provider (this file)
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
    Application Services     UnitOfWork
                                      │
                                      ▼
                                Repositories
                                      │
                                      ▼
                                 Infrastructure

===============================================================================
Design Principles
===============================================================================

• Routers never instantiate Use Cases.

• Use Cases depend only on abstractions.

• Infrastructure dependencies are injected here.

• Every request receives its own transactional Unit of Work.

This approach simplifies testing, promotes Dependency Inversion and keeps the
architecture aligned with the principles of Clean Architecture.
"""

from src.application.use_cases.auth.get_current_user import (
    GetCurrentUserUseCase,
)
from src.application.use_cases.auth.login_user import (
    LoginUserUseCase,
)
from src.application.use_cases.auth.register_user import (
    RegisterUserUseCase,
)
from src.application.use_cases.financial_account.create_financial_account import (
    CreateFinancialAccountUseCase,
)
from src.application.use_cases.financial_account.list_financial_accounts import (
    ListFinancialAccountsUseCase,
)
from src.domain.repositories.unit_of_work import UnitOfWork

from src.infrastructure.database.sqlalchemy_unit_of_work import (
    SqlAlchemyUnitOfWork,
)

from src.application.use_cases.financial_account.get_financial_account import (
    GetFinancialAccountUseCase,
)

from src.application.use_cases.financial_account.update_financial_account import (
    UpdateFinancialAccountUseCase,
)

from .repositories import get_session_factory

from .services import (
    get_password_hasher,
    get_password_verifier,
    get_token_provider,
)


# ============================================================================
# Infrastructure
# ============================================================================


def get_unit_of_work() -> UnitOfWork:
    """
    Creates a new transactional Unit of Work.

    A fresh SQLAlchemy Session is created for each request, ensuring that every
    business operation executes inside its own transactional boundary.

    Returns
    -------
    UnitOfWork
        Concrete SQLAlchemy implementation of the Unit of Work.
    """

    return SqlAlchemyUnitOfWork(
        session_factory=get_session_factory(),
    )


# ============================================================================
# Authentication
# ============================================================================


def get_register_user_use_case() -> RegisterUserUseCase:
    """
    Creates the RegisterUserUseCase.

    Dependencies
    ------------
    • UnitOfWork
    • PasswordHasher
    """

    return RegisterUserUseCase(
        unit_of_work=get_unit_of_work(),
        password_hasher=get_password_hasher(),
    )


def get_login_user_use_case() -> LoginUserUseCase:
    """
    Creates the LoginUserUseCase.

    Dependencies
    ------------
    • UnitOfWork
    • PasswordVerifier
    • TokenProvider
    """

    return LoginUserUseCase(
        unit_of_work=get_unit_of_work(),
        password_verifier=get_password_verifier(),
        token_provider=get_token_provider(),
    )


def get_current_user_use_case() -> GetCurrentUserUseCase:
    """
    Creates the GetCurrentUserUseCase.

    Dependencies
    ------------
    • UnitOfWork
    """

    return GetCurrentUserUseCase(
        unit_of_work=get_unit_of_work(),
    )


# ============================================================================
# Financial Accounts
# ============================================================================


def get_create_financial_account_use_case(
) -> CreateFinancialAccountUseCase:
    """
    Creates the CreateFinancialAccountUseCase.

    Dependencies
    ------------
    • UnitOfWork
    """

    return CreateFinancialAccountUseCase(
        unit_of_work=get_unit_of_work(),
    )


def get_list_financial_accounts_use_case(
) -> ListFinancialAccountsUseCase:
    """
    Creates the ListFinancialAccountsUseCase.

    Dependencies
    ------------
    • UnitOfWork
    """

    return ListFinancialAccountsUseCase(
        unit_of_work=get_unit_of_work(),
    )

def get_get_financial_account_use_case() -> (
    GetFinancialAccountUseCase
):
    """
    Creates the GetFinancialAccountUseCase.

    Purpose
    -------
    Provides the application service responsible for retrieving a single
    financial account owned by the authenticated user.

    Dependencies
    ------------
    • UnitOfWork

    Returns
    -------
    GetFinancialAccountUseCase

        Configured use case ready for dependency injection.
    """

    return GetFinancialAccountUseCase(
        unit_of_work=get_unit_of_work(),
    )

def get_update_financial_account_use_case() -> (
    UpdateFinancialAccountUseCase
):
    """
    Creates the UpdateFinancialAccountUseCase.

    =============================================================================
    Purpose
    =============================================================================

    Provides the application service responsible for updating an existing
    financial account owned by the authenticated user.

    The returned use case is fully configured with its required dependencies
    and is intended to be injected into FastAPI endpoints.

    =============================================================================
    Dependencies
    =============================================================================

    • UnitOfWork

    Returns
    -------
    UpdateFinancialAccountUseCase

        Configured application service ready for dependency injection.
    """

    return UpdateFinancialAccountUseCase(
        unit_of_work=get_unit_of_work(),
    )