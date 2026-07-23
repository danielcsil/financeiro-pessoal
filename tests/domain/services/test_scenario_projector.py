
from datetime import date

from src.domain.entities import (
    CashFlowTimeline,
    FinancialPlan,
    PlanningPeriod,
    Scenario,
    ScenarioType,
)
from src.domain.services import ScenarioProjector
from src.domain.value_objects import Money


def test_should_project_base_scenario():

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
        opening_balance=Money(5000),
        timeline=timeline,
    )

    scenario = Scenario(
        name="Base",
        scenario_type=ScenarioType.BASE,
        plan=plan,
    )

    projection = ScenarioProjector().project(
        scenario
    )

    assert len(projection) == 31
