
from __future__ import annotations

from src.domain.entities import (
    GoalAnalysis,
)


class GoalAnalyzer:

    def analyze(
        self,
        projection,
        goal,
    ) -> GoalAnalysis:

        projected_balance = None

        for day in projection:

            if day.date == goal.target_date:
                projected_balance = day.closing_balance
                break

        if projected_balance is None:
            projected_balance = projection.days[-1].closing_balance

        difference = projected_balance - goal.target_amount

        return GoalAnalysis(
            achieved=difference >= difference.zero(),
            projected_balance=projected_balance,
            target_amount=goal.target_amount,
            difference=difference,
        )
