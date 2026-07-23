
from src.domain.services import FinancialPlanner


def test_should_execute_complete_planning_pipeline(financial_plan):

    planner = FinancialPlanner()

    result = planner.analyze(financial_plan)

    assert result is not None

    assert result.projection is not None

    assert result.liquidity is not None

    assert result.score is not None

    assert result.advisor is not None

    assert result.report is not None


def test_should_return_consistent_result(financial_plan):

    planner = FinancialPlanner()

    result = planner.analyze(financial_plan)

    assert result.score.overall >= 0

    assert result.score.overall <= 100

    assert result.report.score == result.score


def test_should_be_deterministic(financial_plan):

    planner = FinancialPlanner()

    first = planner.analyze(financial_plan)

    second = planner.analyze(financial_plan)

    assert first.score == second.score

    assert first.report.summary == second.report.summary
