
from __future__ import annotations

from src.domain.entities import CreditDependencyAnalysis
from src.domain.value_objects import Money


class CreditDependencyAnalyzer:

    def analyze(self, projection):

        first_day = None
        required_credit = Money.zero()
        days_using_credit = 0

        for day in projection:

            if day.closing_balance.is_negative():

                if first_day is None:
                    first_day = day.date

                days_using_credit += 1

                deficit = -day.closing_balance

                if deficit > required_credit:
                    required_credit = deficit

        return CreditDependencyAnalysis(
            depends_on_credit=first_day is not None,
            first_credit_day=first_day,
            required_credit=required_credit,
            days_using_credit=days_using_credit,
        )
