import pytest

from src.domain.value_objects.email import Email
from src.domain.exceptions import InvalidEmailError


def test_should_normalize_email():
    email = Email("  Daniel@GMAIL.COM ")

    assert str(email) == "daniel@gmail.com"


def test_should_compare_by_value():
    assert Email("A@GMAIL.COM") == Email("a@gmail.com")


def test_should_return_domain():
    email = Email("john@gmail.com")

    assert email.domain == "gmail.com"


def test_should_return_local_part():
    email = Email("john@gmail.com")

    assert email.local_part == "john"


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "abc",
        "@gmail.com",
        "john@",
        "johngmail.com",
        "john@@gmail.com",
    ],
)
def test_should_raise_for_invalid_email(value):
    with pytest.raises(InvalidEmailError):
        Email(value)