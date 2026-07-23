
from decimal import Decimal

from src.domain.value_objects import Money, Percentage


def test_should_create_percentage():
    percentage = Percentage(15)

    assert percentage.to_decimal() == Decimal("15.0000")


def test_should_create_zero_percentage():
    assert Percentage.zero().to_decimal() == Decimal("0.0000")


def test_should_convert_factor():
    percentage = Percentage.from_factor(0.25)

    assert percentage.to_decimal() == Decimal("25.0000")


def test_should_return_factor():
    percentage = Percentage(15)

    assert percentage.factor() == Decimal("0.15")


def test_should_add_percentage():
    result = Percentage(10) + Percentage(5)

    assert result.to_decimal() == Decimal("15.0000")


def test_should_subtract_percentage():
    result = Percentage(15) - Percentage(5)

    assert result.to_decimal() == Decimal("10.0000")


def test_should_apply_percentage_to_money():
    result = Percentage(10).apply(Money(250))

    assert result == Decimal("25.0000")


def test_should_identify_zero():
    assert Percentage.zero().is_zero()


def test_should_identify_positive():
    assert Percentage(5).is_positive()


def test_should_identify_negative():
    assert Percentage(-5).is_negative()


def test_should_compare_equal_percentage():
    assert Percentage(10) == Percentage("10.0000")


def test_should_compare_different_percentage():
    assert Percentage(10) != Percentage(20)
