
from src.domain.services import MinimalInterventionEngine


def test_should_return_none_when_empty():

    engine = MinimalInterventionEngine()

    assert engine.evaluate([], lambda _: 0) is None


def test_should_choose_lowest_score():

    engine = MinimalInterventionEngine()

    scores = {
        "A": 9,
        "B": 2,
        "C": 5,
    }

    result = engine.evaluate(
        ["A", "B", "C"],
        lambda x: scores[x],
    )

    assert result.intervention == "B"
    assert result.score == 2


def test_should_rank_all_interventions():

    engine = MinimalInterventionEngine()

    scores = {
        "A": 7,
        "B": 1,
        "C": 4,
        "D": 3,
    }

    ranking = engine.rank(
        ["A", "B", "C", "D"],
        lambda x: scores[x],
    )

    assert [r.intervention for r in ranking] == [
        "B",
        "D",
        "C",
        "A",
    ]

    assert [r.score for r in ranking] == [
        1,
        3,
        4,
        7,
    ]
