
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import DailyCashFlow, Money


@dataclass(frozen=True, slots=True)
class ProjectionDay:

    date: date
    opening_balance: Money
    daily_cash_flow: DailyCashFlow
    closing_balance: Money

    @property
    def income(self) -> Money:
        return self.daily_cash_flow.income

    @property
    def expense(self) -> Money:
        return self.daily_cash_flow.expense

    @property
    def adjustment(self) -> Money:
        return self.daily_cash_flow.adjustment

    @property
    def net_change(self) -> Money:
        return self.daily_cash_flow.net_change
