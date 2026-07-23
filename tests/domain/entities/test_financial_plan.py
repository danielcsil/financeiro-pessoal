
from datetime import date

from src.domain.entities import (
    CashFlowTimeline,
    FinancialPlan,
    PlanningPeriod,
)
from src.domain.value_objects import Money


def test_should_create_financial_plan():

    period = PlanningPeriod(
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )

    timeline = CashFlowTimeline(
        period.start_date,
        period.end_date,
    )

    plan = FinancialPlan(
        period=period,
        opening_balance=Money(1000),
        timeline=timeline,
    )

    assert plan.period == period
    assert plan.opening_balance == Money(1000)
    assert plan.timeline == timeline
