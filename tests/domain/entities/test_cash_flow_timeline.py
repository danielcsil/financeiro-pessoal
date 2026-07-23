from datetime import date

from src.domain.entities import (
    CashFlowTimeline,
    FinancialPlan,
    PlanningPeriod,
    Scenario,
    ScenarioType,
)
from src.domain.value_objects import Money


def test_should_add_scenario():

    period = PlanningPeriod(
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
    )

    plan = FinancialPlan(
        period=period,
        opening_balance=Money(500),
        timeline=CashFlowTimeline(
            period.start_date,
            period.end_date,
        ),
    )

    scenario = Scenario(
        name="Redução de Gastos",
        scenario_type=ScenarioType.PESSIMISTIC,
    )

    plan.add_scenario(scenario)

    assert len(plan.scenarios) == 1
    assert plan.scenarios[0] == scenario