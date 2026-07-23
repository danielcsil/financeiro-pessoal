
from src.domain.services import CashFlowRecoveryPlanner


def test_should_create_recovery_planner():

    planner = CashFlowRecoveryPlanner()

    assert planner is not None
