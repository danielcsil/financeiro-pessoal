from datetime import date

import pytest

from src.domain.entities import (
    CashFlowTimeline,
    FinancialPlan,
    PlanningPeriod,
)
from src.domain.value_objects import Money


@pytest.fixture
def financial_plan():
    period = PlanningPeriod(
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )

    return FinancialPlan(
        period=period,
        opening_balance=Money(1000),
        timeline=CashFlowTimeline(
            period.start_date,
            period.end_date,
        ),
    )
