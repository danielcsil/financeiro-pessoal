
from src.domain.services import MinimalInterventionEngine


def test_should_return_complete_ranking():

    engine = MinimalInterventionEngine()

    scores = {
        "A": 40,
        "B": 15,
        "C": 25,
    }

    result = engine.recommend_all(
        interventions=["A", "B", "C"],
        evaluator=lambda x: scores[x],
        baseline_score=50,
    )

    assert len(result) == 3

    assert result[0]["intervention"] == "B"
    assert result[1]["intervention"] == "C"
    assert result[2]["intervention"] == "A"


def test_should_return_empty_when_no_candidates():

    engine = MinimalInterventionEngine()

    result = engine.recommend_all(
        interventions=[],
        evaluator=lambda _: 0,
        baseline_score=100,
    )

    assert result == []
