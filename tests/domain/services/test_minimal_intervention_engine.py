
from src.domain.services import MinimalInterventionEngine


def test_should_return_none_when_empty():

    engine = MinimalInterventionEngine()

    result = engine.evaluate([], lambda _: 0)

    assert result is None


def test_should_choose_lowest_score():

    engine = MinimalInterventionEngine()

    interventions = ["A", "B", "C"]

    scores = {
        "A": 8,
        "B": 2,
        "C": 5,
    }

    result = engine.evaluate(
        interventions,
        lambda i: scores[i],
    )

    assert result.intervention == "B"
    assert result.score == 2


def test_should_call_evaluator_for_all_candidates():

    engine = MinimalInterventionEngine()

    calls = []

    def evaluator(value):
        calls.append(value)
        return value

    engine.evaluate([4, 2, 9], evaluator)

    assert calls == [4, 2, 9]
