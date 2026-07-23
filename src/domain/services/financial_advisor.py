
from __future__ import annotations

from src.domain.entities import FinancialAdvice
from src.domain.services import (
    AvailableCashAnalyzer,
    CapitalNeedAnalyzer,
    CashExhaustionAnalyzer,
    CreditDependencyAnalyzer,
)


class FinancialAdvisor:

    def advise(
        self,
        projection,
    ) -> FinancialAdvice:

        messages = []

        exhaustion = CashExhaustionAnalyzer().analyze(projection)

        if exhaustion.exhausted:
            messages.append(
                f"Seu caixa ficará negativo em {exhaustion.exhaustion_date}."
            )

        capital = CapitalNeedAnalyzer().analyze(projection)

        if not capital.already_sufficient:
            messages.append(
                f"Será necessário um capital adicional de {capital.required_capital}."
            )

        credit = CreditDependencyAnalyzer().analyze(projection)

        if credit.depends_on_credit:
            messages.append(
                "Evite assumir novas despesas antes da recuperação do caixa."
            )

        available = AvailableCashAnalyzer().analyze(projection)

        if available.available_to_spend.is_zero():
            messages.append(
                "Não há margem segura para novos gastos."
            )

        if not messages:
            messages.append(
                "A projeção financeira está saudável."
            )

        return FinancialAdvice(messages)
