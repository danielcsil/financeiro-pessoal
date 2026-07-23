
from __future__ import annotations

from src.domain.entities import CashExhaustionAnalysis


class CashExhaustionAnalyzer:

    def analyze(self, projection):

        for day in projection:

            if day.closing_balance.is_negative():

                return CashExhaustionAnalysis(
                    exhausted=True,
                    exhaustion_date=day.date,
                    balance_before_exhaustion=day.opening_balance,
                    negative_balance=day.closing_balance,
                )

        return CashExhaustionAnalysis(
            exhausted=False,
            exhaustion_date=None,
            balance_before_exhaustion=None,
            negative_balance=None,
        )
