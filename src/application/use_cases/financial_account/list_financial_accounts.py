from __future__ import annotations

"""
List Financial Accounts Use Case.
"""

from src.application.dto.financial_account.list_financial_accounts_response import (
    FinancialAccountItemResponse,
    ListFinancialAccountsResponse,
)
from src.domain.repositories.unit_of_work import UnitOfWork


class ListFinancialAccountsUseCase:
    """
    Lists every financial account owned by the authenticated user.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        user_id: str,
    ) -> ListFinancialAccountsResponse:
        """
        Retrieves every financial account belonging to the given user.
        """

        with self._unit_of_work as uow:

            accounts = (
                uow.financial_accounts.find_all_by_user(
                    user_id,
                )
            )

        items = [
            FinancialAccountItemResponse(
                id=account.id,
                name=account.name,
                institution=account.institution,
                account_type=account.account_type.value,
                balance=account.current_balance,
                color=account.color,
                icon=account.icon,
                include_in_cash_flow=account.include_in_cash_flow,
                include_in_net_worth=account.include_in_net_worth,
                active=account.active,
                created_at=account.created_at,
            )
            for account in accounts
        ]

        return ListFinancialAccountsResponse(
            items=items,
            total=len(items),
        )