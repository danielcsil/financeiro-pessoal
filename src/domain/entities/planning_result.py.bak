
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import (
    CashFlowProjection,
    LiquidityAnalysis,
    FinancialHealthScore,
    AdvisorResult,
    AdvisorReport,
    OptimizationResult,
    ScenarioComparison,
)


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
