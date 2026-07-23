from pathlib import Path

ROOT = Path("src/domain/entities")

REPLACEMENTS = {
    "from src.domain.entities import InterventionSimulation":
        "from .intervention_simulation import InterventionSimulation",

    "from src.domain.entities import ProjectionDay":
        "from .projection_day import ProjectionDay",

    "from src.domain.entities import TimelineDay, Transaction":
        (
            "from .timeline_day import TimelineDay\n"
            "from .transaction import Transaction"
        ),

    "from src.domain.entities import FinancialHealthLevel":
        "from .financial_health_level import FinancialHealthLevel",

    "from src.domain.entities import SimulationResult":
        "from .simulation_result import SimulationResult",

    "from src.domain.entities import Account, Category":
        (
            "from .account import Account\n"
            "from .category import Category"
        ),

    "from src.domain.entities import FinancialPlan":
        "from .financial_plan import FinancialPlan",

    "from src.domain.entities import Transaction":
        "from .transaction import Transaction",

    "from src.domain.entities import FinancialHealthScore":
        "from .financial_health_score import FinancialHealthScore",

    "from src.domain.entities import ExpenseNature":
        "from .expense_nature import ExpenseNature",
}


def main():

    total = 0

    for file in ROOT.glob("*.py"):

        text = file.read_text(encoding="utf-8")

        original = text

        for old, new in REPLACEMENTS.items():
            text = text.replace(old, new)

        if text != original:

            backup = file.with_suffix(".py.bak2")
            backup.write_text(original, encoding="utf-8")

            file.write_text(text, encoding="utf-8")

            print(f"✓ {file.name}")

            total += 1

    print()
    print(f"{total} arquivos corrigidos.")


if __name__ == "__main__":
    main()