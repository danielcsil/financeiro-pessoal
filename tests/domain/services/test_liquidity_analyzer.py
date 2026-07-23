
from datetime import date

from src.domain.entities import CashFlowTimeline
from src.domain.services import (
    CashFlowProjector,
    LiquidityAnalyzer,
)
from src.domain.value_objects import Money


def test_should_analyze_positive_projection():

    timeline = CashFlowTimeline(
        date(2026,8,1),
        date(2026,8,5),
    )

    projection = CashFlowProjector().project(
        timeline,
        Money(1000),
    )

    analysis = LiquidityAnalyzer().analyze(
        projection
    )

    assert analysis.minimum_balance == Money(1000)
    assert analysis.maximum_balance == Money(1000)
    assert analysis.ending_balance == Money(1000)

    assert analysis.first_negative_day is None
    assert analysis.negative_days == 0
    assert not analysis.has_negative_balance
