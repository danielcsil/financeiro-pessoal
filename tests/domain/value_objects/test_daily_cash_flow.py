
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


def test_should_calculate_net_change():

    summary = DailyCashFlow(
        income=Money(3500),
        expense=Money(850),
        adjustment=Money(150),
    )

    assert summary.income == Money(3500)
    assert summary.expense == Money(850)
    assert summary.adjustment == Money(150)
    assert summary.net_change == Money(2800)


def test_should_create_zero_summary():

    summary = DailyCashFlow.zero()

    assert summary.income == Money.zero()
    assert summary.expense == Money.zero()
    assert summary.adjustment == Money.zero()
    assert summary.net_change == Money.zero()
