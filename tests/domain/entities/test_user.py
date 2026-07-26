from __future__ import annotations

from src.domain.entities.user import User, UserStatus
from src.domain.value_objects.email import Email
from src.domain.value_objects.password import Password



def test_should_create_user() -> None:
    """
    Should create a user with default values.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    assert user.name == "Daniel"
    assert user.email == Email("daniel@email.com")
    assert user.password.value == "Senha123"

    assert user.status == UserStatus.ACTIVE
    assert user.email_verified is False

    assert user.id is not None
    assert user.created_at is not None
    assert user.updated_at is not None
    assert user.last_login_at is None


def test_should_verify_email() -> None:
    """
    Should mark e-mail as verified.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    user.verify_email()

    assert user.email_verified is True


def test_should_register_login() -> None:
    """
    Should update last login timestamp.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    assert user.last_login_at is None

    user.register_login()

    assert user.last_login_at is not None


def test_should_lock_user() -> None:
    """
    Should lock the account.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    user.lock()

    assert user.status == UserStatus.LOCKED


def test_should_disable_user() -> None:
    """
    Should disable the account.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    user.disable()

    assert user.status == UserStatus.DISABLED


def test_should_activate_user() -> None:
    """
    Should activate the account.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    user.lock()

    user.activate()

    assert user.status == UserStatus.ACTIVE


def test_should_not_be_active_when_email_is_not_verified() -> None:
    """
    User without verified e-mail cannot authenticate.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    assert user.is_active is False


def test_should_be_active_when_email_is_verified() -> None:
    """
    User becomes active after e-mail verification.
    """

    user = User(
        name="Daniel",
        email=Email("daniel@email.com"),
        password=Password("Senha123"),
    )

    user.verify_email()

    assert user.is_active is True