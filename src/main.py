"""
Ponto de entrada da aplicação.
"""

from config.constants import (
    APP_NAME,
    VERSION,
    AUTHOR,
    ORGANIZATION,
)

from config.settings import (
    OUTPUT_DIRECTORY,
)


def main() -> None:

    print("=" * 70)
    print(APP_NAME)
    print("=" * 70)

    print(f"Versão      : {VERSION}")
    print(f"Autor       : {AUTHOR}")
    print(f"Organização : {ORGANIZATION}")
    print(f"Saída       : {OUTPUT_DIRECTORY}")

    print("=" * 70)


if __name__ == "__main__":
    main()
