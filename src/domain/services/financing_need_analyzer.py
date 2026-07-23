
from __future__ import annotations

from src.domain.entities import FinancingNeed


class FinancingNeedAnalyzer:
    """
    Avalia se um gap de liquidez exige
    financiamento externo ou se pode ser
    absorvido naturalmente pelas próximas
    entradas de caixa.
    """

    def analyze(
        self,
        *,
        start_date,
        end_date,
        required_amount,
        financing_required,
        justification,
    ) -> FinancingNeed:

        return FinancingNeed(
            start_date=start_date,
            end_date=end_date,
            required_amount=required_amount,
            financing_required=financing_required,
            justification=justification,
        )
