
from datetime import date

from src.domain.entities import CashFlowTimeline
from src.domain.services import CashFlowProjector
from src.domain.value_objects import Money


def test_should_project_empty_timeline():

    timeline = CashFlowTimeline(
        date(2026,8,1),
        date(2026,8,3),
    )

    projection = CashFlowProjector().project(
        timeline,
        Money(5000),
    )

    assert len(projection)==3

    assert projection.days[0].opening_balance == Money(5000)
    assert projection.days[2].closing_balance == Money(5000)
