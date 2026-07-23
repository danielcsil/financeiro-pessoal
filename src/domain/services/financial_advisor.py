
from __future__ import annotations

from src.domain.services import (
    StrategyGenerator,
    InterventionSimulator,
)


class FinancialAdvisor:
    """
    Coordena todo o processo de tomada de decisão.

    Diagnóstico
        ↓
    Estratégias
        ↓
    Simulações
        ↓
    Ranking
        ↓
    Melhor alternativa
    """

    def __init__(self):

        self._generator = StrategyGenerator()
        self._simulator = InterventionSimulator()


    def recommend(
        self,
        financial_plan,
        diagnosis,
        scorer,
    ):

        strategies = self._generator.generate(
            diagnosis
        )

        ranking = self._simulator.simulate_all(
            financial_plan=financial_plan,
            interventions=strategies,
            scorer=scorer,
        )

        from src.domain.entities import AdvisorResult

        return AdvisorResult(
            best=ranking[0] if ranking else None,
            ranking=ranking,
        )
