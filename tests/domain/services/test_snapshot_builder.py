
from datetime import date

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.services import SnapshotBuilder
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_build_snapshot():

    projection = CashFlowProjection()

    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(1000),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(1500),
        )
    )

    snapshot = SnapshotBuilder().build(projection)

    assert snapshot.initial_balance == Money(1000)
    assert snapshot.final_balance == Money(1500)
