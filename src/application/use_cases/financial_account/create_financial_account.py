from __future__ import annotations

from src.application.dto.financial_account.create_financial_account_request import (
    CreateFinancialAccountRequest,
)
from src.application.dto.financial_account.create_financial_account_response import (
    CreateFinancialAccountResponse,
)
from src.domain.entities.financial_account import FinancialAccount
from src.domain.exceptions.duplicate_financial_account_error import (
    DuplicateFinancialAccountError,
)
from src.domain.repositories.unit_of_work import UnitOfWork


class CreateFinancialAccountUseCase:
    """
    Creates a new financial account for the authenticated user.

    ============================================================================
    Role inside the Application Layer
    ============================================================================

    A Use Case represents a business application action.

    It coordinates the interaction between the presentation layer, the domain
    model and the persistence layer without containing infrastructure details.

    This class does not know:

    • FastAPI
    • SQLAlchemy
    • PostgreSQL
    • JSON
    • HTTP
    • Pydantic

    Its only responsibility is orchestrating the execution of the business
    operation.

    ============================================================================
    Business Rules
    ============================================================================

    The current implementation enforces the following rules:

    1. A user cannot own two financial accounts with the same name.

    2. Every new account starts as active.

    3. The current balance is initialized with the initial balance informed
       during creation.

    4. The account is persisted inside a transactional boundary.

    ============================================================================
    Transaction Boundary
    ============================================================================

    The Use Case depends on a Unit of Work instead of a repository directly.

    This provides a single transactional context for all repositories involved
    in the operation.

    Although this use case currently persists only one aggregate, future
    implementations may require additional operations, such as:

    • creating an opening balance transaction;

    • writing an audit log;

    • publishing a domain event;

    • updating financial projections.

    All these actions should succeed or fail atomically.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        user_id,
        request: CreateFinancialAccountRequest,
    ) -> CreateFinancialAccountResponse:
        """
        Creates and persists a FinancialAccount.

        Parameters
        ----------
        user_id
            Owner of the account.

        request
            Input data required for account creation.

        Returns
        -------
        CreateFinancialAccountResponse

        Raises
        ------
        DuplicateFinancialAccountError

            Raised when another account with the same name already exists for
            the same user.
        """

        repository = self._unit_of_work.financial_accounts

        if repository.exists_by_name(
            user_id=user_id,
            name=request.name,
        ):
            raise DuplicateFinancialAccountError(
                request.name,
            )

        account = FinancialAccount(
            user_id=user_id,
            name=request.name,
            institution=request.institution,
            account_type=request.account_type,
            initial_balance=request.initial_balance,
            current_balance=request.initial_balance,
            color=request.color,
            icon=request.icon,
            include_in_cash_flow=request.include_in_cash_flow,
            include_in_net_worth=request.include_in_net_worth,
        )

        repository.add(account)

        self._unit_of_work.commit()

        return CreateFinancialAccountResponse(
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