
from src.domain.services import InterventionSimulator


def test_should_rank_interventions(financial_plan):

    simulator = InterventionSimulator()

    interventions = [
        "A",
        "B",
        "C",
    ]

    ranking = simulator.simulate_all(
        financial_plan=financial_plan,
        interventions=interventions,
        scorer=lambda simulation: (
            simulation.liquidity.minimum_balance
        ),
    )

    assert len(ranking) == 3

    assert ranking[0].score <= ranking[1].score
    assert ranking[1].score <= ranking[2].score
