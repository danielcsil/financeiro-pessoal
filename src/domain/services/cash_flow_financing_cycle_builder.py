
from __future__ import annotations

from src.domain.entities import CashFlowFinancingCycle


class CashFlowFinancingCycleBuilder:
    """
    Consolida as análises relacionadas ao financiamento
    do fluxo de caixa em um único agregado de domínio.

    Nesta versão inicial define apenas o contrato.
    A composição automática a partir dos analisadores
    existentes será implementada nas próximas iterações.
    """

    def build(
        self,
        *,
        start_date,
        end_date,
        origin,
        maximum_financing_need,
        estimated_recovery_date,
    ) -> CashFlowFinancingCycle:

        return CashFlowFinancingCycle(
            start_date=start_date,
            end_date=end_date,
            origin=origin,
            maximum_financing_need=maximum_financing_need,
            estimated_recovery_date=estimated_recovery_date,
        )
