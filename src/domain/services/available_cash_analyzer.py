
from __future__ import annotations

from src.domain.entities import AvailableCashAnalysis
from src.domain.value_objects import Money


class AvailableCashAnalyzer:

    def analyze(self, projection):

        current_balance = projection.days[0].opening_balance

        minimum_balance = min(
            day.closing_balance
            for day in projection
        )

        available = current_balance - minimum_balance

        if available.is_negative():
            available = Money.zero()

        return AvailableCashAnalysis(
            current_balance=current_balance,
            minimum_future_balance=minimum_balance,
            available_to_spend=available,
        )
