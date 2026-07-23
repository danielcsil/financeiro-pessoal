
from src.domain.services import MinimalInterventionEngine


def test_should_return_recommendation():

    engine = MinimalInterventionEngine()

    scores = {
        "Reduzir lazer": 65,
        "Trocar vencimento": 40,
        "Adiar compra": 80,
    }

    result = engine.recommend(
        interventions=list(scores.keys()),
        evaluator=lambda x: scores[x],
        baseline_score=100,
    )

    assert result["intervention"] == "Trocar vencimento"
    assert result["score"] == 40
    assert result["improvement"] == 60
    assert result["improvement_percent"] == 60.0


def test_should_return_none_when_no_candidates():

    engine = MinimalInterventionEngine()

    result = engine.recommend(
        interventions=[],
        evaluator=lambda _: 0,
        baseline_score=100,
    )

    assert result is None
