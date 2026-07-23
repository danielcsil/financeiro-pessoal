
"""
DailyCashFlow Value Object.
"""

from __future__ import annotations

from dataclasses import dataclass

from .money import Money

@dataclass(frozen=True, slots=True)
class DailyCashFlow:

    income: Money
    expense: Money
    adjustment: Money

    @property
    def net_change(self) -> Money:
        return (
            self.income
            - self.expense
            + self.adjustment
        )

    @classmethod
    def zero(cls) -> "DailyCashFlow":
        return cls(
            income=Money.zero(),
            expense=Money.zero(),
            adjustment=Money.zero(),
        )
