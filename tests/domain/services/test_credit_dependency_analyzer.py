
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import CreditDependencyAnalyzer
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_detect_credit_dependency():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(500),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(200),
        )
    )

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 2),
            opening_balance=Money(200),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(-150),
        )
    )

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 3),
            opening_balance=Money(-150),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(-300),
        )
    )

    analysis = CreditDependencyAnalyzer().analyze(projection)

    assert analysis.depends_on_credit
    assert analysis.first_credit_day == date(2026, 8, 2)
    assert analysis.required_credit == Money(300)
    assert analysis.days_using_credit == 2


def test_should_not_depend_on_credit():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(900),
        )
    )

    analysis = CreditDependencyAnalyzer().analyze(projection)

    assert not analysis.depends_on_credit
