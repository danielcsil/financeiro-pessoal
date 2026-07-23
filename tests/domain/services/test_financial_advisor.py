
from types import SimpleNamespace

from src.domain.services import FinancialAdvisor


def test_should_return_best_strategy(financial_plan):

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
