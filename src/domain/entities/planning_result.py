
from __future__ import annotations

from dataclasses import dataclass

from .advisor_report import AdvisorReport
from .advisor_result import AdvisorResult
from .cash_flow_projection import CashFlowProjection
from .financial_health_score import FinancialHealthScore
from .liquidity_analysis import LiquidityAnalysis
from .optimization_result import OptimizationResult
from .scenario_comparison import ScenarioComparison


@dataclass(frozen=True, slots=True)
class PlanningResult:
    """
    Resultado consolidado do planejamento financeiro.

    Reúne todos os artefatos produzidos pelo pipeline
    completo de apoio à decisão.
    """

    projection: CashFlowProjection

    liquidity: LiquidityAnalysis

    score: FinancialHealthScore

    advisor: AdvisorResult

    optimization: OptimizationResult | None

    comparison: ScenarioComparison | None

    report: AdvisorReport
