
from __future__ import annotations

from src.domain.entities import (
    FinancialStatus,
    FinancialStatusType,
)
from src.domain.value_objects import Money


class FinancialStatusAnalyzer:

    def analyze(
        self,
        balance: Money,
        warning_limit: Money = Money(1000),
    ) -> FinancialStatus:

        if balance.is_negative():
            return FinancialStatus(
                FinancialStatusType.NEGATIVE,
                balance,
            )

        if balance <= warning_limit:
            return FinancialStatus(
                FinancialStatusType.WARNING,
                balance,
            )

        return FinancialStatus(
            FinancialStatusType.HEALTHY,
            balance,
        )
