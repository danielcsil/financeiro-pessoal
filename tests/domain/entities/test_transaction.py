
from datetime import date
from uuid import UUID

import pytest

from src.domain.entities import Account, Category, Transaction
from src.domain.enums import (
    AccountType,
    CategoryType,
    TransactionStatus,
    TransactionType,
)
from src.domain.value_objects import Money


def create_account():
    return Account(
        name="Conta Corrente",
        type=AccountType.CHECKING,
    )


def create_category():
    return Category(
        name="Alimentação",
        type=CategoryType.EXPENSE,
    )


def create_transaction(
    transaction_type=TransactionType.EXPENSE,
):
    return Transaction(
        account=create_account(),
        category=create_category(),
        type=transaction_type,
        amount=Money(100),
        transaction_date=date.today(),
        description="Mercado",
    )


def test_should_create_transaction():
    transaction = create_transaction()

    assert isinstance(transaction.id, UUID)
    assert transaction.status == TransactionStatus.PENDING
    assert transaction.type == TransactionType.EXPENSE


def test_should_not_accept_zero_amount():
    with pytest.raises(ValueError):
        Transaction(
            account=create_account(),
            category=create_category(),
            type=TransactionType.EXPENSE,
            amount=Money.zero(),
            transaction_date=date.today(),
        )


def test_should_post_transaction():
    transaction = create_transaction()
    transaction.post()
    assert transaction.status == TransactionStatus.POSTED


def test_should_cancel_transaction():
    transaction = create_transaction()
    transaction.cancel()
    assert transaction.status == TransactionStatus.CANCELLED


def test_should_reverse_transaction():
    transaction = create_transaction()
    transaction.post()
    transaction.reverse()
    assert transaction.status == TransactionStatus.REVERSED


def test_should_not_post_twice():
    transaction = create_transaction()
    transaction.post()

    with pytest.raises(ValueError):
        transaction.post()


def test_should_not_cancel_posted_transaction():
    transaction = create_transaction()
    transaction.post()

    with pytest.raises(ValueError):
        transaction.cancel()


def test_should_not_reverse_pending_transaction():
    transaction = create_transaction()

    with pytest.raises(ValueError):
        transaction.reverse()


def test_should_change_description():
    transaction = create_transaction()

    transaction.change_description("Supermercado")

    assert transaction.description == "Supermercado"


def test_should_not_allow_external_status_assignment():
    transaction = create_transaction()

    with pytest.raises(AttributeError):
        transaction.status = TransactionStatus.POSTED


def test_should_identify_income_transaction():
    transaction = create_transaction(TransactionType.INCOME)

    assert transaction.is_income()
    assert not transaction.is_expense()
    assert not transaction.is_adjustment()


def test_should_identify_expense_transaction():
    transaction = create_transaction(TransactionType.EXPENSE)

    assert transaction.is_expense()
    assert not transaction.is_income()
    assert not transaction.is_adjustment()


def test_should_identify_adjustment_transaction():
    transaction = create_transaction(TransactionType.ADJUSTMENT)

    assert transaction.is_adjustment()
    assert not transaction.is_income()
    assert not transaction.is_expense()
