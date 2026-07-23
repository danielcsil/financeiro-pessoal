
from datetime import date

from src.domain.entities import CashFlowTimeline


def test_should_create_timeline():

    timeline = CashFlowTimeline(
        date(2026, 8, 1),
        date(2026, 8, 31),
    )

    assert len(timeline.days) == 31
    assert timeline.start_date == date(2026, 8, 1)
    assert timeline.end_date == date(2026, 8, 31)


def test_should_return_day():

    timeline = CashFlowTimeline(
        date(2026, 8, 1),
        date(2026, 8, 31),
    )

    day = timeline.day(date(2026, 8, 15))

    assert day.date == date(2026, 8, 15)
