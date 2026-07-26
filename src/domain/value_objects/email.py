from __future__ import annotations

import re
from dataclasses import dataclass
from src.domain.exceptions import InvalidEmailError

_EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"
)


@dataclass(frozen=True, slots=True)
class Email:
    """
    Value Object que representa um endereço de e-mail.

    Regras:
    - obrigatório
    - removidos espaços nas extremidades
    - armazenado em letras minúsculas
    - comparação por valor
    """

    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()

        if not normalized:
            raise InvalidEmailError("O e-mail é obrigatório.")

        if len(normalized) > 254:
            raise InvalidEmailError("O e-mail possui tamanho inválido.")

        if not _EMAIL_REGEX.fullmatch(normalized):
            raise InvalidEmailError("O e-mail informado é inválido.")

        object.__setattr__(self, "value", normalized)

    @property
    def local_part(self) -> str:
        return self.value.split("@", 1)[0]

    @property
    def domain(self) -> str:
        return self.value.split("@", 1)[1]

    def same_domain(self, other: "Email") -> bool:
        return self.domain == other.domain

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"Email('{self.value}')"