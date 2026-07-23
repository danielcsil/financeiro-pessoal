"""
Ponto de entrada da aplicação.
"""

from config.constants import (
    APP_NAME,
    VERSION,
)

from config.settings import (
    OUTPUT_DIRECTORY,
)


def main() -> None:
    print("=" * 60)
    print(APP_NAME)
    print("=" * 60)
    print(f"Versão : {VERSION}")
    print(f"Saída   : {OUTPUT_DIRECTORY}")
    print("=" * 60)


if __name__ == "__main__":
    main()
