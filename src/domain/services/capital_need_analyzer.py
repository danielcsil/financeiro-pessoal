
from __future__ import annotations

from src.domain.entities import CapitalNeedAnalysis
from src.domain.value_objects import Money


class CapitalNeedAnalyzer:

    def analyze(
        self,
        projection,
        safety_margin: Money = Money.zero(),
    ) -> CapitalNeedAnalysis:

        minimum_balance = min(
            day.closing_balance
            for day in projection
        )

        if minimum_balance >= safety_margin:

            return CapitalNeedAnalysis(
                required_capital=Money.zero(),
                already_sufficient=True,
                safety_margin=safety_margin,
            )

        required = safety_margin - minimum_balance

        return CapitalNeedAnalysis(
            required_capital=required,
            already_sufficient=False,
            safety_margin=safety_margin,
        )
