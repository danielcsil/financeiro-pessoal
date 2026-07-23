
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import ExpenseSimulationService
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_approve_new_expense():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(1000),
        )
    )

    result = ExpenseSimulationService().simulate(
        projection,
        Money(300),
    )

    assert result.approved


def test_should_reject_new_expense():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(200),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(200),
        )
    )

    result = ExpenseSimulationService().simulate(
        projection,
        Money(500),
    )

    assert not result.approved
