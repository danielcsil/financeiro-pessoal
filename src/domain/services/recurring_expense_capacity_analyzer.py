
from __future__ import annotations

from src.domain.entities import (
    RecurringExpenseCapacityAnalysis,
)
from src.domain.value_objects import Money


class RecurringExpenseCapacityAnalyzer:

    def analyze(
        self,
        projection,
        safety_margin: Money = Money.zero(),
    ) -> RecurringExpenseCapacityAnalysis:

        minimum_balance = min(
            day.closing_balance
            for day in projection
        )

        available = minimum_balance - safety_margin

        if available.is_negative():
            available = Money.zero()

        return RecurringExpenseCapacityAnalysis(
            maximum_recurring_expense=available,
            safety_margin=safety_margin,
            can_assume_new_expense=available > Money.zero(),
        )
