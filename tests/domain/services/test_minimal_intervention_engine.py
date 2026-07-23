
from src.domain.services import (
    EvaluatedIntervention,
    MinimalInterventionEngine,
)


def test_should_explain_intervention():

    engine = MinimalInterventionEngine()

    candidate = EvaluatedIntervention(
        intervention="Reduzir lazer",
        score=70,
    )

    result = engine.explain(
        candidate,
        baseline_score=100,
    )

    assert result["intervention"] == "Reduzir lazer"
    assert result["score"] == 70
    assert result["baseline_score"] == 100
    assert result["improvement"] == 30
    assert result["improvement_percent"] == 30.0


def test_should_handle_zero_baseline():

    engine = MinimalInterventionEngine()

    candidate = EvaluatedIntervention(
        intervention="Nenhuma",
        score=0,
    )

    result = engine.explain(
        candidate,
        baseline_score=0,
    )

    assert result["improvement_percent"] == 0.0
