
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import AvailableCashAnalyzer
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_calculate_available_cash():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(900),
        )
    )

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 2),
            opening_balance=Money(900),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(700),
        )
    )

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 3),
            opening_balance=Money(700),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(800),
        )
    )

    analysis = AvailableCashAnalyzer().analyze(
        projection
    )

    assert analysis.available_to_spend == Money(300)
