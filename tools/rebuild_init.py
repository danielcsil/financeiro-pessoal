"""
Reconstrói automaticamente o arquivo __init__.py de um pacote Python.

Exemplo de uso:

python tools/rebuild_init.py src/domain/entities
python tools/rebuild_init.py src/domain/services

O script:
- encontra todos os módulos .py do pacote;
- ignora __init__.py e arquivos privados (_*);
- gera os imports;
- gera automaticamente o __all__;
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path


def public_classes(module: Path) -> list[str]:
    """
    Retorna as classes públicas definidas no módulo.
    """
    tree = ast.parse(module.read_text(encoding="utf-8"))

    classes = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            if not node.name.startswith("_"):
                classes.append(node.name)

    return classes


def rebuild(package: Path):

    modules = []

    for file in sorted(package.glob("*.py")):

        if file.name == "__init__.py":
            continue

        if file.stem.startswith("_"):
            continue

        classes = public_classes(file)

        if not classes:
            continue

        modules.append((file.stem, classes))

    imports = []
    exported = []

    for module, classes in modules:

        imports.append(
            f"from .{module} import {', '.join(classes)}"
        )

        exported.extend(classes)

    exported.sort()

    content = []

    content.extend(imports)

    content.append("")
    content.append("__all__ = [")

    for name in exported:
        content.append(f'    "{name}",')

    content.append("]")

    output = "\n".join(content) + "\n"

    (package / "__init__.py").write_text(
        output,
        encoding="utf-8",
    )

    print(f"✓ {package}/__init__.py reconstruído")
    print(f"  {len(exported)} classes exportadas")


def main():

    if len(sys.argv) != 2:
        print("Uso:")
        print("python tools/rebuild_init.py <pacote>")
        raise SystemExit(1)

    package = Path(sys.argv[1])

    if not package.exists():
        raise FileNotFoundError(package)

    rebuild(package)


if __name__ == "__main__":
    main()