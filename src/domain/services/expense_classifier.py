
from __future__ import annotations

from src.domain.entities import ExpenseNature


class ExpenseClassifier:

    def is_essential(self, transaction) -> bool:
        return transaction.nature == ExpenseNature.ESSENTIAL

    def is_flexible(self, transaction) -> bool:
        return transaction.nature == ExpenseNature.FLEXIBLE

    def is_discretionary(self, transaction) -> bool:
        return transaction.nature == ExpenseNature.DISCRETIONARY
