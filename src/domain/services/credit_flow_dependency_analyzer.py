
from __future__ import annotations

from src.domain.entities import CreditFlowDependency
from src.domain.services import LiquidityGapAnalyzer


class CreditFlowDependencyAnalyzer:

    def analyze(self, projection):

        gaps = LiquidityGapAnalyzer().analyze(projection)

        if not gaps:
            return None

        return CreditFlowDependency(
            start_date=gaps[0].date,
            end_date=gaps[-1].date,
            financed_amount=max(
                gap.required_amount
                for gap in gaps
            ),
        )
