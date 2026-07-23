
from datetime import date

from src.domain.entities import PlanningPeriod


def test_should_calculate_total_days():

    period = PlanningPeriod(
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 31),
    )

    assert period.total_days == 31
