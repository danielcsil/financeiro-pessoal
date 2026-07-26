from __future__ import annotations

import pytest

from src.domain.exceptions import InvalidPasswordError
from src.domain.value_objects.password import Password


def test_should_create_valid_password() -> None:
    password = Password("Senha123")

    assert password.value == "Senha123"


def test_should_trim_password() -> None:
    password = Password("   Senha123   ")

    assert password.value == "Senha123"


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "1234567",
    ],
)
def test_should_reject_invalid_password(
    value: str,
) -> None:
    with pytest.raises(InvalidPasswordError):
        Password(value)