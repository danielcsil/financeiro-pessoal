"""
Configurações gerais da aplicação.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIRECTORY = PROJECT_ROOT / "output"

OUTPUT_DIRECTORY.mkdir(exist_ok=True)
