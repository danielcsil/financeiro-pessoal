
from uuid import UUID

import pytest

from src.domain.entities import Category
from src.domain.enums import CategoryType


def test_should_create_category():
    category = Category(
        name="Alimentação",
        type=CategoryType.EXPENSE,
    )

    assert isinstance(category.id, UUID)
    assert category.name == "Alimentação"
    assert category.type == CategoryType.EXPENSE
    assert category.active is True


def test_should_create_income_category():
    category = Category(
        name="Salário",
        type=CategoryType.INCOME,
    )

    assert category.type == CategoryType.INCOME


def test_should_rename_category():
    category = Category(
        name="Mercado",
        type=CategoryType.EXPENSE,
    )

    category.rename("Supermercado")

    assert category.name == "Supermercado"


def test_should_not_accept_empty_name():
    category = Category(
        name="Teste",
        type=CategoryType.EXPENSE,
    )

    with pytest.raises(ValueError):
        category.rename("   ")


def test_should_deactivate_category():
    category = Category(
        name="Lazer",
        type=CategoryType.EXPENSE,
    )

    category.deactivate()

    assert category.active is False


def test_should_activate_category():
    category = Category(
        name="Lazer",
        type=CategoryType.EXPENSE,
    )

    category.deactivate()
    category.activate()

    assert category.active is True


def test_should_not_allow_external_name_assignment():
    category = Category(
        name="Teste",
        type=CategoryType.EXPENSE,
    )

    with pytest.raises(AttributeError):
        category.name = "Outra"


def test_should_not_allow_external_active_assignment():
    category = Category(
        name="Teste",
        type=CategoryType.EXPENSE,
    )

    with pytest.raises(AttributeError):
        category.active = False


def test_should_not_allow_external_type_assignment():
    category = Category(
        name="Teste",
        type=CategoryType.EXPENSE,
    )

    with pytest.raises(AttributeError):
        category.type = CategoryType.INCOME
