
from __future__ import annotations

from copy import deepcopy


class ScenarioApplier:

    def apply(
        self,
        timeline,
        adjustments,
    ):

        timeline = deepcopy(timeline)

        for adjustment in adjustments:

            if adjustment.adjustment_type.name == "ADD_TRANSACTION":
                timeline.add_transaction(
                    adjustment.transaction
                )

        return timeline
