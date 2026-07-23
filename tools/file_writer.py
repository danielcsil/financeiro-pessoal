"""
Ferramenta para criação automática de arquivos.
"""

from pathlib import Path


def write_files(files: dict[str, str]) -> None:
    """
    Cria ou atualiza vários arquivos.
    """

    for filename, content in files.items():

        file = Path(filename)

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        print(f"[OK] {filename}")
