
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CashFlowMetrics:

    minimum_balance: Money

    maximum_liquidity_gap: Money

    required_capital: Money

    available_cash: Money

    credit_dependency_months: int

    recovery_date: date | None
