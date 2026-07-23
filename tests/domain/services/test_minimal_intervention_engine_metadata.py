
from src.domain.services import MinimalInterventionEngine


def test_should_attach_metadata():

    engine = MinimalInterventionEngine()

    scores = {
        "Trocar vencimento": 10,
    }

    result = engine.evaluate(
        interventions=["Trocar vencimento"],
        evaluator=lambda x: scores[x],
        metadata_provider=lambda x: {
            "days_shift": 5,
            "cash_gain": 820,
        },
    )

    assert result.metadata["days_shift"] == 5
    assert result.metadata["cash_gain"] == 820


def test_should_include_metadata_in_explanation():

    engine = MinimalInterventionEngine()

    candidate = engine.evaluate(
        interventions=["A"],
        evaluator=lambda _: 15,
        metadata_provider=lambda _: {
            "origin": "simulation",
        },
    )

    explanation = engine.explain(
        candidate,
        baseline_score=20,
    )

    assert explanation["metadata"]["origin"] == "simulation"
