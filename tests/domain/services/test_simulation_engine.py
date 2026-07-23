
from src.domain.services import SimulationEngine


def test_should_keep_baseline_simulation_information(financial_plan):

    engine = SimulationEngine()

    result = engine.simulate(
        financial_plan=financial_plan,
        adjustments=[],
    )

    assert result.has_baseline
    assert result.baseline_projection is not None
    assert result.baseline_liquidity is not None
