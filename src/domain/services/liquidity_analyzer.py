
from __future__ import annotations

from src.domain.entities import LiquidityAnalysis


class LiquidityAnalyzer:

    def analyze(
        self,
        projection,
    ) -> LiquidityAnalysis:

        minimum = projection.days[0].closing_balance
        maximum = minimum

        ending = projection.days[-1].closing_balance

        first_negative = None
        negative_days = 0

        for day in projection:

            balance = day.closing_balance

            if balance < minimum:
                minimum = balance

            if balance > maximum:
                maximum = balance

            if balance.is_negative():

                negative_days += 1

                if first_negative is None:
                    first_negative = day.date

        return LiquidityAnalysis(
            minimum_balance=minimum,
            maximum_balance=maximum,
            ending_balance=ending,
            first_negative_day=first_negative,
            negative_days=negative_days,
            has_negative_balance=negative_days > 0,
        )
