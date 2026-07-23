
from datetime import date

from src.domain.entities import (
    CashFlowTimeline,
    ScenarioAdjustment,
    ScenarioAdjustmentType,
    Transaction,
    Account,
    Category,
)
from src.domain.services import ScenarioApplier
from src.domain.value_objects import Money


def test_should_apply_transaction_to_timeline():

    timeline = CashFlowTimeline(
        date(2026, 8, 1),
        date(2026, 8, 31),
    )

    transaction = Transaction(
        description="Salário",
        amount=Money(5000),
        account=Account("Conta"),
        category=Category("Receita"),
        date=date(2026, 8, 5),
    )

    adjustment = ScenarioAdjustment(
        adjustment_type=ScenarioAdjustmentType.ADD_TRANSACTION,
        transaction=transaction,
    )

    result = ScenarioApplier().apply(
        timeline,
        [adjustment],
    )

    assert len(result.day(date(2026, 8, 5))) == 1
