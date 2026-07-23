
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class FinancialGoal:

    name: str

    target_amount: Money

    target_date: date
