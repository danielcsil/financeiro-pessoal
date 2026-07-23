
from src.domain.services import FinancialPlanner


def test_should_execute_complete_pipeline(financial_plan):

    planner = FinancialPlanner()

    result = planner.analyze(financial_plan)

    assert result.projection is not None

    assert result.liquidity is not None

    assert result.score is not None

    assert result.advisor is not None

    assert result.report is not None
