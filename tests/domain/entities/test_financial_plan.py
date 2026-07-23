from datetime import date

from src.domain.entities import (
    CashFlowTimeline,
    FinancialGoal,
    FinancialPlan,
    PlanningPeriod,
)
from src.domain.value_objects import Money


def test_should_add_goal():

    period = PlanningPeriod(
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
    )

    plan = FinancialPlan(
        period=period,
        opening_balance=Money(1000),
        timeline=CashFlowTimeline(
            period.start_date,
            period.end_date,
        ),
    )

    goal = FinancialGoal(
        name="Reserva",
        target_amount=Money(10000),
        target_date=date(2026, 12, 31),
    )

    plan.add_goal(goal)

    assert len(plan.goals) == 1
    assert plan.goals[0] == goal