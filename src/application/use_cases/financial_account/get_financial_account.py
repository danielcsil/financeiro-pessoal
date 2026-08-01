from __future__ import annotations

"""
Get Financial Account Use Case.

===============================================================================
Purpose
===============================================================================

Retrieves a single financial account owned by a specific user.

Unlike the list operation, this use case returns exactly one account and
guarantees that the authenticated user is allowed to access it.

===============================================================================
Business Rules
===============================================================================

The use case validates that:

    • the financial account exists;

    • the account belongs to the authenticated user.

If either validation fails, a domain exception is raised.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

GetFinancialAccountUseCase

        │

        ▼

UnitOfWork

        │

        ▼

FinancialAccountRepository

===============================================================================
Transaction
===============================================================================

This use case performs only read operations.

No transaction is committed.
"""

from uuid import UUID

from src.application.dto.financial_account.get_financial_account_response import (
    GetFinancialAccountResponse,
)
from src.domain.exceptions.financial_account_not_found_error import (
    FinancialAccountNotFoundError,
)
from src.domain.repositories.unit_of_work import (
    UnitOfWork,
)


class GetFinancialAccountUseCase:
    """
    Retrieves a financial account belonging to a user.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        *,
        user_id: UUID,
        account_id: UUID,
    ) -> GetFinancialAccountResponse:
        """
        Retrieves a financial account owned by the authenticated user.

        Parameters
        ----------
        user_id:
            Identifier of the authenticated user.

        account_id:
            Identifier of the requested financial account.

        Returns
        -------
        GetFinancialAccountResponse
            Complete information about the requested financial account.

        Raises
        ------
        FinancialAccountNotFoundError
            Raised when:

            • the account does not exist;

            • the account belongs to another user.
        """

        with self._unit_of_work as uow:

            account = (
                uow.financial_accounts.find_by_id(
                    account_id,
                )
            )

            if account is None:
                raise FinancialAccountNotFoundError()

            if account.user_id != user_id:
                raise FinancialAccountNotFoundError()

            return GetFinancialAccountResponse(
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
            )