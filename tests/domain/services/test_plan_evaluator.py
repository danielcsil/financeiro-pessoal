
from src.domain.services import PlanEvaluator


def test_should_create_plan_evaluator():

    evaluator = PlanEvaluator()

    assert evaluator is not None
