from __future__ import annotations

import ast
import re
import shutil
import sys
from pathlib import Path


def discover_classes(package: Path) -> dict[str, str]:
    """
    Retorna um mapa:
        Classe -> módulo
    Exemplo:
        Account -> account
        FinancialPlan -> financial_plan
    """

    mapping = {}

    for file in sorted(package.glob("*.py")):

        if file.name == "__init__.py":
            continue

        if file.stem.startswith("_"):
            continue

        tree = ast.parse(file.read_text(encoding="utf-8"))

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                mapping[node.name] = file.stem

    return mapping


def fix_file(file: Path, package_name: str, mapping: dict[str, str]) -> bool:

    text = file.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"from\s+src\.domain\.{package_name}\s+import\s+\((.*?)\)",
        re.DOTALL,
    )

    changed = False

    def replace(match):

        nonlocal changed

        body = match.group(1)

        names = []

        for line in body.splitlines():

            line = line.strip()

            if not line:
                continue

            line = line.rstrip(",")

            if line:
                names.append(line)

        grouped = {}

        for name in names:

            if name not in mapping:
                print(
                    f"[AVISO] {name} não encontrado em {package_name}"
                )
                continue

            grouped.setdefault(mapping[name], []).append(name)

        imports = []

        for module in sorted(grouped):

            classes = ", ".join(sorted(grouped[module]))

            imports.append(
                f"from .{module} import {classes}"
            )

        changed = True

        return "\n".join(imports)

    new_text = pattern.sub(replace, text)

    if changed:

        shutil.copy2(file, file.with_suffix(".py.bak"))

        file.write_text(
            new_text,
            encoding="utf-8",
        )

    return changed


def process(package: Path):

    mapping = discover_classes(package)

    total = 0

    for file in sorted(package.glob("*.py")):

        if fix_file(
            file,
            package.name,
            mapping,
        ):
            print(f"✓ {file.name}")
            total += 1

    print()
    print(f"{total} arquivos modificados.")


def main():

    if len(sys.argv) != 2:

        print(
            "Uso:\n"
            "python tools/fix_internal_imports.py src/domain/entities"
        )

        raise SystemExit(1)

    package = Path(sys.argv[1])

    if not package.exists():
        raise FileNotFoundError(package)

    process(package)


if __name__ == "__main__":
    main()