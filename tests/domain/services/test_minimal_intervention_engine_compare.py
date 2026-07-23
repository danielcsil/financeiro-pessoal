
from src.domain.services import MinimalInterventionEngine


def test_should_compare_candidates():

    engine = MinimalInterventionEngine()

    scores = {
        "A": 15,
        "B": 40,
        "C": 25,
    }

    ranking = engine.rank(
        interventions=["A", "B", "C"],
        evaluator=lambda x: scores[x],
    )

    comparison = engine.compare(ranking)

    assert comparison[0]["gap_to_best"] == 0
    assert comparison[1]["gap_to_best"] == 10
    assert comparison[2]["gap_to_best"] == 25


def test_should_compare_empty_list():

    engine = MinimalInterventionEngine()

    assert engine.compare([]) == []
