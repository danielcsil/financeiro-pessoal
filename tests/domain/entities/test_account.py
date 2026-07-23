
from uuid import UUID

import pytest

from src.domain.entities import Account
from src.domain.enums import AccountStatus, AccountType
from src.domain.value_objects import Money


def test_should_create_account():
    account = Account(
        name="Banco do Brasil",
        type=AccountType.CHECKING,
    )

    assert isinstance(account.id, UUID)
    assert account.name == "Banco do Brasil"
    assert account.type == AccountType.CHECKING
    assert account.status == AccountStatus.ACTIVE
    assert account.balance == Money.zero()


def test_should_rename_account():
    account = Account(
        name="Conta Antiga",
        type=AccountType.CHECKING,
    )

    account.rename("Conta Nova")

    assert account.name == "Conta Nova"


def test_should_not_accept_empty_name():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    with pytest.raises(ValueError):
        account.rename("   ")


def test_should_activate_account():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    account.deactivate()
    account.activate()

    assert account.status == AccountStatus.ACTIVE


def test_should_deactivate_account():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    account.deactivate()

    assert account.status == AccountStatus.INACTIVE


def test_should_close_account():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    account.close()

    assert account.status == AccountStatus.CLOSED


def test_should_start_with_zero_balance():
    account = Account(
        name="Conta",
        type=AccountType.SAVINGS,
    )

    assert account.balance == Money.zero()

def test_should_not_allow_external_name_assignment():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    with pytest.raises(AttributeError):
        account.name = "Outra"

def test_should_not_allow_external_balance_assignment():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    with pytest.raises(AttributeError):
        account.balance = Money(100)


def test_should_not_allow_external_status_assignment():
    account = Account(
        name="Conta",
        type=AccountType.CHECKING,
    )

    with pytest.raises(AttributeError):
        account.status = AccountStatus.CLOSED
