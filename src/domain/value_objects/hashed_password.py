from __future__ import annotations

from dataclasses import dataclass

from src.domain.exceptions.invalid_password_hash_error import (
    InvalidPasswordHashError,
)


@dataclass(frozen=True)
class HashedPassword:
    """
    Represents a hashed password.
    """

    value: str

    def __post_init__(self) -> None:
        password_hash = self.value.strip()

        if not password_hash:
            raise InvalidPasswordHashError(
                "Password hash is required."
            )

        object.__setattr__(self, "value", password_hash)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return "HashedPassword(******)"
