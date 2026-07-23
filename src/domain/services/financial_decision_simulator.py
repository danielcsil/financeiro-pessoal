
from __future__ import annotations

from src.domain.entities import FinancialDecision


class FinancialDecisionSimulator:

    def simulate(
        self,
        projection,
        decision: FinancialDecision,
    ):
        """
        Aplica uma decisão financeira sobre a projeção.

        Nesta primeira versão, o simulador apenas define
        o contrato do serviço. Nos próximos commits ele
        passará a alterar a linha do tempo, recalcular a
        projeção e comparar os resultados.
        """
        return projection
