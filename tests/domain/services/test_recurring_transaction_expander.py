
from datetime import date

from src.domain.entities import (
    Account,
    Category,
    RecurrenceFrequency,
    RecurringTransaction,
)
from src.domain.services import RecurringTransactionExpander
from src.domain.value_objects import Money


def test_should_expand_weekly_transaction():

    recurring = RecurringTransaction(
        description="Academia",
        amount=Money(100),
        account=Account("Conta"),
        category=Category("Saúde"),
        start_date=date(2026,8,1),
        end_date=date(2026,8,15),
        frequency=RecurrenceFrequency.WEEKLY,
    )

    transactions = RecurringTransactionExpander().expand(
        recurring
    )

    assert len(transactions) == 3
