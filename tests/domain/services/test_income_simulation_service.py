
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import IncomeSimulationService
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_increase_capacity_with_new_income():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(700),
        )
    )

    result = IncomeSimulationService().simulate(
        projection,
        Money(500),
    )

    assert result.simulated_income == Money(500)
    assert result.additional_margin == Money(1200)
