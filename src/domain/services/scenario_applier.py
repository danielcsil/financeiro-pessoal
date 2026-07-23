from __future__ import annotations

from copy import deepcopy

from src.domain.entities.scenario_adjustment_type import (
    ScenarioAdjustmentType,
)


class ScenarioApplier:

    def apply(
        self,
        timeline,
        adjustments,
    ):

        timeline = deepcopy(timeline)

        for adjustment in adjustments:

            if (
                adjustment.adjustment_type
                == ScenarioAdjustmentType.ADD_TRANSACTION
            ):
                timeline.add_transaction(
                    adjustment.transaction
                )

            elif (
                adjustment.adjustment_type
                == ScenarioAdjustmentType.REMOVE_TRANSACTION
            ):
                day = timeline.day(
                    adjustment.transaction.transaction_date
                )

                day._transactions = [
                    t
                    for t in day._transactions
                    if t.id != adjustment.transaction.id
                ]

        return timeline