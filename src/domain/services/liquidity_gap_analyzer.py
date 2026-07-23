
from __future__ import annotations

from src.domain.entities import LiquidityGap
from src.domain.value_objects import Money


class LiquidityGapAnalyzer:

    def analyze(
        self,
        projection,
    ) -> list[LiquidityGap]:

        gaps = []

        for day in projection:

            if day.closing_balance < Money.zero():

                gaps.append(
                    LiquidityGap(
                        date=day.date,
                        required_amount=abs(day.closing_balance),
                    )
                )

        return gaps
