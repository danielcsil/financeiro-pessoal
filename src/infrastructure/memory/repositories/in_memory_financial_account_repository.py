from __future__ import annotations

from uuid import UUID

from src.domain.entities.financial_account import FinancialAccount
from src.domain.repositories.financial_account_repository import (
    FinancialAccountRepository,
)


class InMemoryFinancialAccountRepository(
    FinancialAccountRepository,
):
    """
    In-memory implementation of FinancialAccountRepository.

    Intended for unit tests.
    """

    def __init__(self) -> None:
        self._accounts: dict[
            UUID,
            FinancialAccount,
        ] = {}

    def add(
        self,
        account: FinancialAccount,
    ) -> None:
        self._accounts[
            account.id
        ] = account

    def update(
        self,
        account: FinancialAccount,
    ) -> None:
        self._accounts[
            account.id
        ] = account

    def find_by_id(
        self,
        account_id: UUID,
    ) -> FinancialAccount | None:
        return self._accounts.get(
            account_id,
        )

    def find_all_by_user(
        self,
        user_id: UUID,
    ) -> list[FinancialAccount]:

        return sorted(
            [
                account
                for account in self._accounts.values()
                if (
                    account.user_id == user_id
                    and account.active
                )
            ],
            key=lambda account: account.name,
        )

    def exists_by_name(
        self,
        user_id: UUID,
        name: str,
    ) -> bool:

        return any(
            account.user_id == user_id
            and account.name == name
            and account.active
            for account in self._accounts.values()
        )

    def remove(
        self,
        account: FinancialAccount,
    ) -> None:

        stored = self._accounts.get(
            account.id,
        )

        if stored is None:
            return

        stored.deactivate()