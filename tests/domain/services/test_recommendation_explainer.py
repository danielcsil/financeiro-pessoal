
from types import SimpleNamespace

from src.domain.entities import FinancialHealthScore
from src.domain.services import RecommendationExplainer


def test_should_generate_report():

    explainer = RecommendationExplainer()

    score = FinancialHealthScore(
        overall=87,
        liquidity=92,
        reserve=80,
        credit_dependency=74,
        stability=88,
        risk=90,
    )

    advisor_result = SimpleNamespace(
        best=SimpleNamespace(
            intervention=SimpleNamespace(
                description="Alterar vencimento do cartão"
            )
        )
    )

    report = explainer.create_report(
        score,
        advisor_result,
    )

    assert report.score.overall == 87

    assert "87" in report.summary

    assert len(report.highlights) == 5


def test_should_handle_empty_recommendation():

    explainer = RecommendationExplainer()

    score = FinancialHealthScore(
        overall=100,
        liquidity=100,
        reserve=100,
        credit_dependency=100,
        stability=100,
        risk=100,
    )

    advisor_result = SimpleNamespace(
        best=None
    )

    report = explainer.create_report(
        score,
        advisor_result,
    )

    assert report.highlights == ()
