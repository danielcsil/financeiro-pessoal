from __future__ import annotations

from datetime import date

from src.domain.enums import TransactionType
from src.domain.value_objects import Money

from .transaction import Transaction


class TimelineDay:
    """
    Representa um único dia da linha do tempo financeira.

    Conhece apenas os eventos ocorridos no dia.
    """

    def __init__(self, day: date):
        self._date = day
        self._transactions: list[Transaction] = []

    @property
    def date(self) -> date:
        return self._date

    @property
    def transactions(self) -> tuple[Transaction, ...]:
        return tuple(self._transactions)

    def add_transaction(
        self,
        transaction: Transaction,
    ) -> None:

        if transaction.transaction_date != self._date:
            raise ValueError(
                "Transaction date does not match TimelineDay."
            )

        self._transactions.append(transaction)

    def income(self) -> Money:
        total = Money.zero()

        for transaction in self._transactions:
            if transaction.type == TransactionType.INCOME:
                total += transaction.amount

        return total

    def expense(self) -> Money:
        total = Money.zero()

        for transaction in self._transactions:
            if transaction.type == TransactionType.EXPENSE:
                total += transaction.amount

        return total

    def balance_change(self) -> Money:
        return self.income() - self.expense()

    def __len__(self) -> int:
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __str__(self) -> str:
        return self._date.isoformat()