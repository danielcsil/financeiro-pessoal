
from src.domain.services import ScenarioComparator


def test_should_create_scenario_comparator():

    comparator = ScenarioComparator()

    assert comparator is not None
