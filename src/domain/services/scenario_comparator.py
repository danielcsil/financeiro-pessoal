
from __future__ import annotations

from src.domain.entities import (
    ScenarioComparison,
)


class ScenarioComparator:
    """
    Compara dois cenários financeiros.

    O comparador trabalha sobre indicadores
    consolidados, independentemente de como eles
    foram produzidos.
    """

    def compare(
        self,
        current_score,
        projected_score,
        current_metrics,
        projected_metrics,
    ) -> ScenarioComparison:

        return ScenarioComparison(

            current=current_score,

            projected=projected_score,

            score_gain=(
                projected_score.overall
                - current_score.overall
            ),

            liquidity_gain=(
                projected_metrics.minimum_balance
                - current_metrics.minimum_balance
            ),

            credit_reduction=(
                current_metrics.credit_used
                - projected_metrics.credit_used
            ),

            negative_days_reduction=(
                current_metrics.negative_days
                - projected_metrics.negative_days
            ),
        )
