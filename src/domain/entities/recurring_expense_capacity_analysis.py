
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class RecurringExpenseCapacityAnalysis:

    maximum_recurring_expense: Money

    safety_margin: Money

    can_assume_new_expense: bool
