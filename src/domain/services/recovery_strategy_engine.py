
from __future__ import annotations

from src.domain.entities import RecoveryStrategy


class RecoveryStrategyEngine:
    """
    Gera estratégias candidatas de recuperação.

    Nesta primeira versão o serviço define o contrato.
    Futuramente utilizará o ciclo de financiamento,
    métricas do fluxo e simuladores para produzir
    estratégias automaticamente.
    """

    def evaluate(
        self,
        *,
        name,
        description,
        expected_benefit,
        recommended=True,
    ) -> RecoveryStrategy:

        return RecoveryStrategy(
            name=name,
            description=description,
            expected_benefit=expected_benefit,
            recommended=recommended,
        )
