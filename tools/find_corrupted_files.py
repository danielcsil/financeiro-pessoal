from pathlib import Path

ROOT = Path("src")

KEYWORDS = [
    "# ...",
    "Acrescente",
    "Atualize",
    "Adicione",
    "Substitua",
    "Insira",
    "Novo atributo",
    "novo atributo",
]

for file in ROOT.rglob("*.py"):
    text = file.read_text(encoding="utf-8", errors="ignore")

    for keyword in KEYWORDS:
        if keyword in text:
            print(file)
            break