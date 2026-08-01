from __future__ import annotations

"""
Update Financial Account Use Case.

===============================================================================
Purpose
===============================================================================

Updates an existing financial account owned by the authenticated user.

This use case is responsible for validating ownership, enforcing business
constraints and persisting the updated state of a financial account.

===============================================================================
Business Rules
===============================================================================

Before updating the account, the following validations are performed:

    • the financial account must exist;

    • the financial account must belong to the authenticated user;

    • another account with the same name cannot already exist for the same
      user.

If any validation fails, a domain exception is raised.

===============================================================================
Architecture
===============================================================================

Presentation Layer

        │

        ▼

UpdateFinancialAccountUseCase

        │

        ▼

UnitOfWork

        │

        ▼

FinancialAccountRepository

===============================================================================
Transaction
===============================================================================

This use case modifies persistent state.

The transaction is committed only after every validation succeeds.
"""

from src.application.dto.financial_account.update_financial_account_request import (
    UpdateFinancialAccountRequest,
)
from src.application.dto.financial_account.update_financial_account_response import (
    UpdateFinancialAccountResponse,
)
from src.domain.exceptions.duplicate_financial_account_error import (
    DuplicateFinancialAccountError,
)
from src.domain.exceptions.financial_account_not_found_error import (
    FinancialAccountNotFoundError,
)
from src.domain.repositories.unit_of_work import (
    UnitOfWork,
)


class UpdateFinancialAccountUseCase:
    """
    Updates an existing financial account.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: UpdateFinancialAccountRequest,
    ) -> UpdateFinancialAccountResponse:
        """
        Updates a financial account.

        Parameters
        ----------
        request:
            Information describing the desired modifications.

        Returns
        -------
        UpdateFinancialAccountResponse
            Updated financial account.

        Raises
        ------
        FinancialAccountNotFoundError

            If the account does not exist or does not belong to the user.

        DuplicateFinancialAccountError

            If another account already uses the same name.
        """

        with self._unit_of_work as uow:

            # --------------------------------------------------------------
            # Retrieve account
            # --------------------------------------------------------------

            account = uow.financial_accounts.find_by_id(
                request.account_id,
            )

            if account is None:
                raise FinancialAccountNotFoundError()

            if account.user_id != request.user_id:
                raise FinancialAccountNotFoundError()

            # --------------------------------------------------------------
            # Validate duplicate name
            # --------------------------------------------------------------

            if (
                account.name != request.name
                and uow.financial_accounts.exists_by_name(
                    request.user_id,
                    request.name,
                )
            ):
                raise DuplicateFinancialAccountError()

            # --------------------------------------------------------------
            # Update entity
            # --------------------------------------------------------------

            account.name = request.name
            account.institution = request.institution
            account.account_type = request.account_type
            account.color = request.color
            account.icon = request.icon
            account.include_in_cash_flow = (
                request.include_in_cash_flow
            )
            account.include_in_net_worth = (
                request.include_in_net_worth
            )

            uow.financial_accounts.update(
                account,
            )

            uow.commit()

            # --------------------------------------------------------------
            # Build response DTO
            # --------------------------------------------------------------

            return UpdateFinancialAccountResponse(
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