
from __future__ import annotations

from src.domain.entities import FinancialSnapshot
from src.domain.services import LiquidityAnalyzer


class SnapshotBuilder:

    def build(self, projection) -> FinancialSnapshot:

        liquidity = LiquidityAnalyzer().analyze(projection)

        return FinancialSnapshot(
            initial_balance=projection.days[0].opening_balance,
            final_balance=liquidity.ending_balance,
            minimum_balance=liquidity.minimum_balance,
            maximum_balance=liquidity.maximum_balance,
            first_negative_date=liquidity.first_negative_day,
        )
