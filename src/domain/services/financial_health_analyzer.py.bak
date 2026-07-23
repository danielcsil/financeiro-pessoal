
from __future__ import annotations

from src.domain.entities import (
    FinancialHealth,
    FinancialHealthLevel,
)
from src.domain.services import (
    CapitalNeedAnalyzer,
    CreditDependencyAnalyzer,
)


class FinancialHealthAnalyzer:

    def analyze(
        self,
        projection,
    ) -> FinancialHealth:

        capital = CapitalNeedAnalyzer().analyze(projection)
        credit = CreditDependencyAnalyzer().analyze(projection)

        if credit.depends_on_credit:
            return FinancialHealth(
                level=FinancialHealthLevel.CRITICAL,
                summary="Há dependência de crédito prevista."
            )

        if not capital.already_sufficient:
            return FinancialHealth(
                level=FinancialHealthLevel.ATTENTION,
                summary="Será necessário capital adicional."
            )

        return FinancialHealth(
            level=FinancialHealthLevel.HEALTHY,
            summary="A projeção apresenta uma situação financeira saudável."
        )
