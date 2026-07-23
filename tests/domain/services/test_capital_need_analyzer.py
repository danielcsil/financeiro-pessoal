
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import CapitalNeedAnalyzer
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_calculate_required_capital():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(400),
        )
    )

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 2),
            opening_balance=Money(400),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(-250),
        )
    )

    analysis = CapitalNeedAnalyzer().analyze(
        projection
    )

    assert analysis.required_capital == Money(250)
    assert not analysis.already_sufficient


def test_should_detect_sufficient_capital():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(800),
        )
    )

    analysis = CapitalNeedAnalyzer().analyze(
        projection
    )

    assert analysis.required_capital == Money.zero()
    assert analysis.already_sufficient
