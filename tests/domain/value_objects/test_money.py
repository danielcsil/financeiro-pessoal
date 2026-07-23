
from decimal import Decimal

import pytest

from src.domain.value_objects import Money


def test_should_create_money():
    money = Money(10)

    assert money.to_decimal() == Decimal("10.00")


def test_should_round_to_two_decimal_places():
    money = Money("10.129")

    assert money.to_decimal() == Decimal("10.13")


def test_should_create_zero_money():
    assert Money.zero().to_decimal() == Decimal("0.00")


def test_should_add_money():
    a = Money(10)
    b = Money(15.50)

    result = a + b

    assert result.to_decimal() == Decimal("25.50")


def test_should_subtract_money():
    a = Money(20)
    b = Money(7.25)

    result = a - b

    assert result.to_decimal() == Decimal("12.75")


def test_should_multiply_money():
    money = Money(10)

    result = money * 3

    assert result.to_decimal() == Decimal("30.00")


def test_should_divide_money():
    money = Money(10)

    result = money / 4

    assert result.to_decimal() == Decimal("2.50")


def test_should_negate_money():
    money = -Money(10)

    assert money.to_decimal() == Decimal("-10.00")


def test_should_return_absolute_money():
    money = abs(Money(-10))

    assert money.to_decimal() == Decimal("10.00")


def test_should_identify_zero():
    assert Money.zero().is_zero()


def test_should_identify_positive():
    assert Money(5).is_positive()


def test_should_identify_negative():
    assert Money(-5).is_negative()


def test_should_compare_equal_money():
    assert Money(10) == Money("10.00")


def test_should_compare_different_money():
    assert Money(10) != Money(11)


def test_should_copy_money():
    money = Money(100)

    copied = money.copy()

    assert copied == money
    assert copied is not money


def test_should_be_immutable():
    money = Money(10)

    with pytest.raises(Exception):
        money.value = Decimal("20.00")
