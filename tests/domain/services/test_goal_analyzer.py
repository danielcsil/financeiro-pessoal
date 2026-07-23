
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    FinancialGoal,
    ProjectionDay,
)
from src.domain.services import GoalAnalyzer
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_achieve_goal():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(5000),
        )
    )

    goal = FinancialGoal(
        name="Reserva",
        target_amount=Money(4000),
        target_date=date(2026, 8, 1),
    )

    analysis = GoalAnalyzer().analyze(
        projection,
        goal,
    )

    assert analysis.achieved
    assert analysis.difference == Money(1000)
