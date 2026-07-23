from datetime import date
from types import SimpleNamespace

from src.domain.entities import (
    Account,
    CashFlowTimeline,
    Category,
    FinancialPlan,
    PlanningPeriod,
)

from src.domain.enums import (
    AccountType,
    CategoryType,
)

from src.domain.services import FinancialAdvisor
from src.domain.value_objects import Money


def create_financial_plan() -> FinancialPlan:
    period = PlanningPeriod(
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
    )

    return FinancialPlan(
        period=period,
        opening_balance=Money(1000),
        timeline=CashFlowTimeline(
            period.start_date,
            period.end_date,
        ),
    )


def create_account() -> Account:
    return Account(
        name="Conta Corrente",
        type=AccountType.CHECKING,
    )


def create_income_category() -> Category:
    return Category(
        name="Receita",
        type=CategoryType.INCOME,
    )


def test_should_return_best_strategy():

    financial_plan = create_financial_plan()

    advisor = FinancialAdvisor()

    diagnosis = SimpleNamespace(
        has_financing_dependency=True,
        has_negative_balance=True,
    )

    result = advisor.recommend(
        financial_plan=financial_plan,
        diagnosis=diagnosis,
        scorer=lambda simulation: (
            simulation.liquidity.minimum_balance
        ),
    )

    assert result.best is not None
    assert len(result.ranking) >= 1


def test_should_keep_best_as_first():

    financial_plan = create_financial_plan()

    advisor = FinancialAdvisor()

    diagnosis = SimpleNamespace(
        has_financing_dependency=True,
        has_negative_balance=False,
    )

    result = advisor.recommend(
        financial_plan=financial_plan,
        diagnosis=diagnosis,
        scorer=lambda simulation: (
            simulation.liquidity.minimum_balance
        ),
    )

    assert result.best == result.ranking[0]