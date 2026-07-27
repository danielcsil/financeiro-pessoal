import pytest

from src.domain.exceptions.invalid_password_hash_error import (
    InvalidPasswordHashError,
)
from src.domain.value_objects.hashed_password import HashedPassword


def test_should_create_hashed_password() -> None:
    password = HashedPassword("$2b$12$abcdefghijklmnopqrstuv")

    assert password.value == "$2b$12$abcdefghijklmnopqrstuv"


def test_should_trim_hashed_password() -> None:
    password = HashedPassword("  $2b$12$abcdefghijklmnopqrstuv  ")

    assert password.value == "$2b$12$abcdefghijklmnopqrstuv"


def test_should_format_hashed_password_repr() -> None:
    password = HashedPassword("$2b$12$abcdefghijklmnopqrstuv")

    assert repr(password) == "HashedPassword(******)"


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
