
from __future__ import annotations

from src.domain.entities import ScenarioComparison


class ScenarioComparator:

    def compare(
        self,
        original_metrics,
        simulated_metrics,
    ) -> ScenarioComparison:

        gap_reduction = (
            original_metrics.max_gap
            - simulated_metrics.max_gap
        )

        recommendation = (
            "RECOMMENDED"
            if gap_reduction > gap_reduction.zero()
            else "NOT_RECOMMENDED"
        )

        return ScenarioComparison(
            original_max_gap=original_metrics.max_gap,
            simulated_max_gap=simulated_metrics.max_gap,
            gap_reduction=gap_reduction,
            original_recovery_months=original_metrics.recovery_months,
            simulated_recovery_months=simulated_metrics.recovery_months,
            recommendation=recommendation,
        )
