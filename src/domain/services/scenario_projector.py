
from __future__ import annotations

from .cash_flow_projector import CashFlowProjector

class ScenarioProjector:

    def __init__(self):

        self._projector = CashFlowProjector()

    def project(self, scenario):

        return self._projector.project(
            scenario.plan.timeline,
            scenario.plan.opening_balance,
        )
