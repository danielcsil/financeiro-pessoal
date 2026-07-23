from __future__ import annotations

from .intervention_planner import InterventionPlanner
from .simulation_engine import SimulationEngine
from .strategy_generator import StrategyGenerator


class FinancialAdvisor:
    """
    Coordena todo o processo de tomada de decisão.

    Diagnóstico
        ↓
    Estratégias
        ↓
    Planejamento das intervenções
        ↓
    Simulações
        ↓
    Ranking
        ↓
    Melhor alternativa
    """

    def __init__(self):

        self._generator = StrategyGenerator()
        self._planner = InterventionPlanner()

    def recommend(
        self,
        financial_plan,
        diagnosis,
        scorer,
    ):

        strategies = self._generator.generate(
            financial_plan,
            diagnosis,
        )

        engine = SimulationEngine()
        ranking = []

        from src.domain.entities import AdvisorResult, InterventionSimulation

        for strategy in strategies:
            adjustment_groups = self._planner.build(
                financial_plan,
                [strategy],
            )

            adjustments = adjustment_groups[0] if adjustment_groups else []

            simulation = engine.simulate(
                financial_plan=financial_plan,
                adjustments=adjustments,
            )

            ranking.append(
                InterventionSimulation(
                    intervention=strategy,
                    result=simulation,
                    score=scorer(simulation),
                )
            )

        ranking.sort(key=lambda item: item.score)

        return AdvisorResult(
            best=ranking[0] if ranking else None,
            ranking=ranking,
        )

    def analyze(self, financial_plan):
        diagnosis = self._build_diagnosis(financial_plan)

        return self.recommend(
            financial_plan=financial_plan,
            diagnosis=diagnosis,
            scorer=lambda simulation: simulation.liquidity.minimum_balance,
        )

    def _build_diagnosis(self, financial_plan):
        from types import SimpleNamespace

        baseline = SimulationEngine().simulate(
            financial_plan=financial_plan,
            adjustments=[],
        )

        return SimpleNamespace(
            has_financing_dependency=False,
            has_negative_balance=baseline.liquidity.has_negative_balance,
        )
