
from src.domain.services import MinimalInterventionEngine


def test_should_return_none_when_empty():

    engine = MinimalInterventionEngine()

    assert engine.evaluate([]) is None


def test_should_return_first_intervention():

    engine = MinimalInterventionEngine()

    result = engine.evaluate(["A","B"])

    assert result == "A"
