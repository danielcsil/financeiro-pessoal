
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import CashExhaustionAnalyzer
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_detect_cash_exhaustion():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026,8,1),
            opening_balance=Money(500),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(100),
        )
    )

    projection.add_day(
        ProjectionDay(
            date=date(2026,8,2),
            opening_balance=Money(100),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(-50),
        )
    )

    analysis = CashExhaustionAnalyzer().analyze(
        projection
    )

    assert analysis.exhausted
    assert analysis.exhaustion_date == date(2026,8,2)
    assert analysis.negative_balance == Money(-50)


def test_should_not_detect_cash_exhaustion():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026,8,1),
            opening_balance=Money(500),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(400),
        )
    )

    analysis = CashExhaustionAnalyzer().analyze(
        projection
    )

    assert not analysis.exhausted
