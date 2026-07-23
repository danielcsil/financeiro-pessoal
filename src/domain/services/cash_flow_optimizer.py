
from __future__ import annotations

from itertools import combinations

from src.domain.entities import OptimizationResult
from .intervention_simulator import InterventionSimulator

class CashFlowOptimizer:
    """
    Procura a melhor combinação de intervenções.

    Nesta primeira versão são avaliadas combinações
    de uma e duas intervenções.
    """

    def optimize(
        self,
        financial_plan,
        interventions,
        scorer,
        max_combination_size: int = 2,
    ) -> OptimizationResult:

        simulator = InterventionSimulator()

        evaluated = []

        for size in range(1, max_combination_size + 1):

            for combo in combinations(interventions, size):

                ranking = simulator.simulate_all(
                    financial_plan=financial_plan,
                    interventions=[list(combo)],
                    scorer=scorer,
                )

                if ranking:
                    evaluated.append(ranking[0])

        evaluated.sort(key=lambda item: item.score)

        return OptimizationResult(
            best=evaluated[0] if evaluated else None,
            evaluated_combinations=len(evaluated),
            combinations=tuple(evaluated),
        )
