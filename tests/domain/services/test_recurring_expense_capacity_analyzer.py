
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import (
    RecurringExpenseCapacityAnalyzer,
)
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_calculate_recurring_capacity():

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
            closing_balance=Money(650),
        )
    )

    analysis = RecurringExpenseCapacityAnalyzer().analyze(
        projection
    )

    assert analysis.maximum_recurring_expense == Money(650)
    assert analysis.can_assume_new_expense


def test_should_not_allow_new_expense():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(200),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(-50),
        )
    )

    analysis = RecurringExpenseCapacityAnalyzer().analyze(
        projection
    )

    assert analysis.maximum_recurring_expense == Money.zero()
    assert not analysis.can_assume_new_expense
