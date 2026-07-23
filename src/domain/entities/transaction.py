
from __future__ import annotations

from datetime import date
from uuid import UUID, uuid4

from src.domain.entities import Account, Category
from src.domain.enums import TransactionStatus
from src.domain.value_objects import Money


class Transaction:

    def __init__(
        self,
        account: Account,
        category: Category,
        amount: Money,
        transaction_date: date,
        description: str = "",
        id: UUID | None = None,
    ):
        if amount.is_zero():
            raise ValueError("Transaction amount cannot be zero.")

        self._id = id or uuid4()
        self._account = account
        self._category = category
        self._amount = amount
        self._transaction_date = transaction_date
        self._description = description.strip()
        self._status = TransactionStatus.PENDING

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def account(self) -> Account:
        return self._account

    @property
    def category(self) -> Category:
        return self._category

    @property
    def amount(self) -> Money:
        return self._amount

    @property
    def transaction_date(self) -> date:
        return self._transaction_date

    @property
    def description(self) -> str:
        return self._description

    @property
    def status(self) -> TransactionStatus:
        return self._status

    def change_description(self, description: str) -> None:
        self._description = description.strip()

    def post(self) -> None:
        if self._status != TransactionStatus.PENDING:
            raise ValueError("Only pending transactions can be posted.")
        self._status = TransactionStatus.POSTED

    def cancel(self) -> None:
        if self._status != TransactionStatus.PENDING:
            raise ValueError("Only pending transactions can be cancelled.")
        self._status = TransactionStatus.CANCELLED

    def reverse(self) -> None:
        if self._status != TransactionStatus.POSTED:
            raise ValueError("Only posted transactions can be reversed.")
        self._status = TransactionStatus.REVERSED

    def __str__(self) -> str:
        return self.description
