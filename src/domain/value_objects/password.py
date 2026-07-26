from __future__ import annotations

from dataclasses import dataclass

from src.domain.exceptions import InvalidPasswordError


@dataclass(frozen=True)
class Password:
    """
    Represents a valid user password.
    """

    value: str

    def __post_init__(self) -> None:
        password = self.value.strip()

        if not password:
            raise InvalidPasswordError(
                "Password is required."
            )

        if len(password) < 8:
            raise InvalidPasswordError(
                "Password must contain at least 8 characters."
            )

        object.__setattr__(self, "value", password)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return "Password(******)"