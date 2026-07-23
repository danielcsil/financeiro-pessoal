
from datetime import date

import pytest

from src.domain.entities import (
    Account,
    Category,
    TimelineDay,
    Transaction,
)
from src.domain.enums import (
    AccountType,
    CategoryType,
    TransactionType,
)
from src.domain.value_objects import Money


def account():
    return Account(
        name="Conta",
        type=AccountType.CHECKING,
    )


def income_category():
    return Category(
        name="Salário",
        type=CategoryType.INCOME,
    )


def expense_category():
    return Category(
        name="Mercado",
        type=CategoryType.EXPENSE,
    )


def test_should_add_transactions():

    day = TimelineDay(date(2026, 8, 1))

    income = Transaction(
        account=account(),
        category=income_category(),
        type=TransactionType.INCOME,
        amount=Money(3000),
        transaction_date=day.date,
    )

    expense = Transaction(
        account=account(),
        category=expense_category(),
        type=TransactionType.EXPENSE,
        amount=Money(500),
        transaction_date=day.date,
    )

    day.add_transaction(income)
    day.add_transaction(expense)

    assert len(day.transactions) == 2
    assert day.income() == Money(3000)
    assert day.expense() == Money(500)
    assert day.balance_change() == Money(2500)


def test_should_reject_transaction_from_other_day():

    day = TimelineDay(date(2026, 8, 1))

    transaction = Transaction(
        account=account(),
        category=expense_category(),
        type=TransactionType.EXPENSE,
        amount=Money(100),
        transaction_date=date(2026, 8, 2),
    )

    with pytest.raises(ValueError):
        day.add_transaction(transaction)
