
from src.domain.entities import LiquidityAnalysis
from src.domain.services import RecommendationEngine
from src.domain.value_objects import Money


def test_should_not_generate_recommendations():

    analysis = LiquidityAnalysis(
        minimum_balance=Money(1000),
        maximum_balance=Money(2000),
        ending_balance=Money(1500),
        first_negative_day=None,
        negative_days=0,
        has_negative_balance=False,
    )

    recommendations = RecommendationEngine().generate(
        analysis
    )

    assert recommendations == []


def test_should_generate_negative_balance_warning():

    analysis = LiquidityAnalysis(
        minimum_balance=Money(-500),
        maximum_balance=Money(1000),
        ending_balance=Money(-200),
        first_negative_day=None,
        negative_days=10,
        has_negative_balance=True,
    )

    recommendations = RecommendationEngine().generate(
        analysis
    )

    assert len(recommendations) == 3
