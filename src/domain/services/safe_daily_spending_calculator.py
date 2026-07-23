
from __future__ import annotations

from src.domain.entities import SafeDailySpending


class SafeDailySpendingCalculator:

    def calculate(
        self,
        available_cash,
        remaining_days,
    ) -> SafeDailySpending:

        if remaining_days <= 0:
            daily_limit = available_cash
        else:
            daily_limit = available_cash / remaining_days

        return SafeDailySpending(
            available_today=available_cash,
            remaining_days=remaining_days,
            recommended_daily_limit=daily_limit,
        )
