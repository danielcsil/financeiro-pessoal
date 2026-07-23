
from __future__ import annotations

from enum import Enum


class TransactionType(Enum):
    """
    Representa o tipo de um lançamento financeiro.

    Transferências entre contas são modeladas por uma entidade própria
    (Transfer), composta por duas transações relacionadas.
    """

    INCOME = "income"
    EXPENSE = "expense"
    ADJUSTMENT = "adjustment"

    @property
    def is_income(self) -> bool:
        return self is TransactionType.INCOME

    @property
    def is_expense(self) -> bool:
        return self is TransactionType.EXPENSE

    @property
    def is_adjustment(self) -> bool:
        return self is TransactionType.ADJUSTMENT
