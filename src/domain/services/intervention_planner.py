from __future__ import annotations

from src.domain.entities import ScenarioAdjustment
from src.domain.entities.scenario_adjustment_type import (
    ScenarioAdjustmentType,
)


class InterventionPlanner:
    """
    Converte GeneratedStrategy em ScenarioAdjustment.

    Nesta primeira versão apenas estratégias de adiamento
    de despesas são suportadas.
    """

    def build(
        self,
        financial_plan,
        strategies,
    ):

        interventions = []

        for strategy in strategies:

            if strategy.type != "POSTPONE_EXPENSE":
                continue

            transaction = strategy.payload

            if transaction is None:
                continue

            interventions.append(
                [
                    ScenarioAdjustment(
                        adjustment_type=ScenarioAdjustmentType.REMOVE_TRANSACTION,
                        transaction=transaction,
                    )
                ]
            )

        return interventions