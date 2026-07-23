
from __future__ import annotations

from src.domain.entities import LiquidityCycleOrigin


class LiquidityCycleOriginAnalyzer:
    """
    Identifica o evento que iniciou o ciclo de perda de liquidez.

    Nesta primeira versão, define o contrato do serviço.
    Nas próximas iterações, utilizará LiquidityEvent,
    LiquidityGap e CashFlowProjection para reconstruir
    a cadeia causal do ciclo.
    """

    def analyze(
        self,
        *,
        start_date,
        triggering_event,
        explanation,
    ) -> LiquidityCycleOrigin:

        return LiquidityCycleOrigin(
            start_date=start_date,
            triggering_event=triggering_event,
            explanation=explanation,
        )
