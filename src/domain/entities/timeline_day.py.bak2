
from __future__ import annotations

from datetime import date

from src.domain.entities import Transaction


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

    def __len__(self) -> int:
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __str__(self) -> str:
        return self._date.isoformat()
