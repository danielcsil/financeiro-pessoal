
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import LiquidityGapAnalyzer
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_detect_liquidity_gap():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 10),
            opening_balance=Money(200),
            daily_cash_flow=DailyCashFlow(
                income=Money.zero(),
                expense=Money(500),
                adjustment=Money.zero(),
            ),
            closing_balance=Money(-300),
        )
    )

    gaps = LiquidityGapAnalyzer().analyze(projection)

    assert len(gaps) == 1
    assert gaps[0].required_amount == Money(300)
