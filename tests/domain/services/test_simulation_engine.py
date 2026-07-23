
from src.domain.services import SimulationEngine


def test_should_execute_simulation():

    engine = SimulationEngine()

    assert engine is not None
