from __future__ import annotations

from domain.exceptions.invalid_password_hash_error import InvalidPasswordHashError
import pytest

from src.domain.value_objects.hashed_password import HashedPassword


def test_should_create_hashed_password() -> None:
    password = HashedPassword("$2b$12$abcdefghijklmnopqrstuv")

    assert password.value == "$2b$12$abcdefghijklmnopqrstuv"


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
    ],
)
def test_should_reject_empty_hash(
    value: str,
) -> None:
    with pytest.raises(InvalidPasswordHashError):
        HashedPassword(value)