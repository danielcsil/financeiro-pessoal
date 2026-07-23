
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class FinancialSnapshot:

    initial_balance: Money

    final_balance: Money

    minimum_balance: Money

    maximum_balance: Money

    first_negative_date: date | None
