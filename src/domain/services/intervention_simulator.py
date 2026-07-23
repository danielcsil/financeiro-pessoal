
from __future__ import annotations

from src.domain.entities import InterventionSimulation
from .simulation_engine import SimulationEngine

class InterventionSimulator:

    def simulate_all(
        self,
        financial_plan,
        interventions,
        scorer,
    ):

        simulations = []

        engine = SimulationEngine()

        for intervention in interventions:
            adjustments = (
                intervention
                if isinstance(intervention, (list, tuple))
                else []
            )

            result = engine.simulate(
                financial_plan=financial_plan,
                adjustments=adjustments,
            )

            simulations.append(
                InterventionSimulation(
                    intervention=intervention,
                    result=result,
                    score=scorer(result),
                )
            )

        simulations.sort(key=lambda item: item.score)

        return simulations
