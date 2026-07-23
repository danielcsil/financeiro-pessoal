
from __future__ import annotations

from src.domain.entities import CashFlowMetrics


class CashFlowMetricsBuilder:
    """
    Consolida os principais indicadores produzidos
    pelos analisadores do domínio em um único objeto.

    Nesta primeira versão o builder define o contrato.
    A integração com os analisadores será feita de forma
    incremental nos próximos commits.
    """

    def build(
        self,
        *,
        minimum_balance,
        maximum_liquidity_gap,
        required_capital,
        available_cash,
        credit_dependency_months,
        recovery_date,
    ) -> CashFlowMetrics:

        return CashFlowMetrics(
            minimum_balance=minimum_balance,
            maximum_liquidity_gap=maximum_liquidity_gap,
            required_capital=required_capital,
            available_cash=available_cash,
            credit_dependency_months=credit_dependency_months,
            recovery_date=recovery_date,
        )
