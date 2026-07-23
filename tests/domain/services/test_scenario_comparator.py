
from types import SimpleNamespace

from src.domain.entities import FinancialHealthScore
from src.domain.services import ScenarioComparator


def test_should_compare_scenarios():

    comparator = ScenarioComparator()

    current_score = FinancialHealthScore(
        overall=74,
        liquidity=70,
        reserve=80,
        credit_dependency=60,
        stability=75,
        risk=85,
    )

    projected_score = FinancialHealthScore(
        overall=89,
        liquidity=92,
        reserve=84,
        credit_dependency=88,
        stability=90,
        risk=91,
    )

    current_metrics = SimpleNamespace(
        minimum_balance=-850,
        credit_used=1250,
        negative_days=9,
    )

    projected_metrics = SimpleNamespace(
        minimum_balance=320,
        credit_used=180,
        negative_days=0,
    )

    comparison = comparator.compare(
        current_score,
        projected_score,
        current_metrics,
        projected_metrics,
    )

    assert comparison.score_gain == 15
    assert comparison.liquidity_gain == 1170
    assert comparison.credit_reduction == 1070
    assert comparison.negative_days_reduction == 9
