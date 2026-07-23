
from __future__ import annotations

from datetime import date

from src.domain.entities import Transaction
from src.domain.value_objects import Money


class TimelineDay:
    """
    Representa um único dia da linha do tempo financeira.

    Esta classe conhece apenas os eventos (transações) ocorridos
    no dia. Informações como saldo inicial e saldo final são
    calculadas pelo CashFlowEngine.
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

    def add_transaction(self, transaction: Transaction) -> None:
        if transaction.transaction_date != self._date:
            raise ValueError(
                "Transaction date does not match TimelineDay."
            )

        self._transactions.append(transaction)

    @property
    def income(self) -> Money:
        total = Money.zero()

        for transaction in self._transactions:
            if transaction.is_income():
                total += transaction.amount

        return total

    @property
    def expense(self) -> Money:
        total = Money.zero()

        for transaction in self._transactions:
            if transaction.is_expense():
                total += transaction.amount

        return total

    @property
    def adjustment(self) -> Money:
        total = Money.zero()

        for transaction in self._transactions:
            if transaction.is_adjustment():
                total += transaction.amount

        return total

    @property
    def net_change(self) -> Money:
        return (
            self.income
            - self.expense
            + self.adjustment
        )

    def __len__(self) -> int:
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __str__(self) -> str:
        return self._date.isoformat()
