
from __future__ import annotations

from src.domain.services import (
    CashFlowProjector,
    LiquidityAnalyzer,
    FinancialHealthScorer,
    FinancialAdvisor,
    RecommendationExplainer,
    ScenarioComparator,
    CashFlowOptimizer,
)


class FinancialPlanner:
    """
    Fachada da API pública do domínio.

    Esta classe centraliza o pipeline completo de
    planejamento financeiro, ocultando a complexidade
    dos serviços internos.
    """

    def __init__(self):

        self.projector = CashFlowProjector()
        self.liquidity = LiquidityAnalyzer()
        self.scorer = FinancialHealthScorer()
        self.advisor = FinancialAdvisor()
        self.explainer = RecommendationExplainer()
        self.comparator = ScenarioComparator()
        self.optimizer = CashFlowOptimizer()

    def analyze(self, financial_plan):
        """
        Executa o fluxo completo de planejamento financeiro.

        Nesta primeira versão o método atua como ponto único
        de entrada da API pública do domínio. A integração
        completa entre todos os componentes será evoluída
        gradualmente sem alterar a interface pública.
        """

        projection = self.projector.project(financial_plan)

        liquidity = self.liquidity.analyze(projection)

        return {
            "projection": projection,
            "liquidity": liquidity,
        }
