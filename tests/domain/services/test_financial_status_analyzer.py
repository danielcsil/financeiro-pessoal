
from src.domain.entities import FinancialStatusType
from src.domain.services import FinancialStatusAnalyzer
from src.domain.value_objects import Money


def test_should_return_healthy():

    result = FinancialStatusAnalyzer().analyze(
        Money(5000)
    )

    assert result.status == FinancialStatusType.HEALTHY


def test_should_return_warning():

    result = FinancialStatusAnalyzer().analyze(
        Money(500)
    )

    assert result.status == FinancialStatusType.WARNING


def test_should_return_negative():

    result = FinancialStatusAnalyzer().analyze(
        Money(-1)
    )

    assert result.status == FinancialStatusType.NEGATIVE
