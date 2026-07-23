
from src.domain.services import FinancialHealthScorer


def test_should_calculate_overall_score():

    scorer = FinancialHealthScorer()

    score = scorer.calculate(
        liquidity=90,
        reserve=80,
        credit_dependency=70,
        stability=85,
        risk=95,
    )

    assert score.overall == 84

    assert score.liquidity == 90
    assert score.reserve == 80
    assert score.credit_dependency == 70
    assert score.stability == 85
    assert score.risk == 95


def test_should_keep_scores_between_zero_and_hundred():

    scorer = FinancialHealthScorer()

    score = scorer.calculate(
        liquidity=100,
        reserve=100,
        credit_dependency=100,
        stability=100,
        risk=100,
    )

    assert score.overall == 100
