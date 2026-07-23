
from __future__ import annotations

from src.domain.entities import LiquidityEvent


class LiquidityEventAnalyzer:

    def analyze(
        self,
        timeline,
        threshold,
    ) -> list[LiquidityEvent]:

        events = []

        for day in timeline:

            for transaction in day:

                if abs(transaction.amount) >= threshold:

                    events.append(
                        LiquidityEvent(
                            date=day.date,
                            description=transaction.description,
                            impact=transaction.amount,
                        )
                    )

        return events
