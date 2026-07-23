
from src.domain.services import MinimalInterventionEngine


def test_should_ignore_invalid_interventions():

    engine = MinimalInterventionEngine()

    scores = {
        "A": 20,
        "B": 5,
        "C": 1,
    }

    valid = {
        "A": True,
        "B": False,
        "C": True,
    }

    result = engine.recommend(
        interventions=["A", "B", "C"],
        evaluator=lambda x: scores[x],
        validator=lambda x: valid[x],
        baseline_score=30,
    )

    assert result["intervention"] == "C"


def test_should_return_none_when_all_invalid():

    engine = MinimalInterventionEngine()

    result = engine.recommend(
        interventions=["A", "B"],
        evaluator=lambda _: 0,
        validator=lambda _: False,
        baseline_score=100,
    )

    assert result is None
