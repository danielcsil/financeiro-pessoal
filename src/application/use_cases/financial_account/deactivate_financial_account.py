from __future__ import annotations

"""
Deactivate Financial Account Use Case.

===============================================================================
Purpose
===============================================================================

Deactivates an existing financial account owned by the authenticated user.

A deactivated account remains stored in the system, preserving every historical
transaction and financial report while preventing future operations.

===============================================================================
Business Rules
===============================================================================

The use case validates that:

    • the financial account exists;

    • the financial account belongs to the authenticated user.

If any validation fails, a domain exception is raised.

===============================================================================
Transaction
===============================================================================

This use case modifies persistent state.

The transaction is committed after the account is successfully deactivated.
"""

from uuid import UUID

from src.domain.exceptions.financial_account_not_found_error import (
    FinancialAccountNotFoundError,
)
from src.domain.repositories.unit_of_work import (
    UnitOfWork,
)


class DeactivateFinancialAccountUseCase:
    """
    Deactivates an existing financial account.
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
    ) -> None:
        """
        Deactivates a financial account.
        """

        with self._unit_of_work as uow:

            account = uow.financial_accounts.find_by_id(
                account_id,
            )

            if account is None:
                raise FinancialAccountNotFoundError()

            if account.user_id != user_id:
                raise FinancialAccountNotFoundError()

            account.active = False

            uow.financial_accounts.update(
                account,
            )

            uow.commit()