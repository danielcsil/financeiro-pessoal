from __future__ import annotations

from src.domain.entities.user import User, UserStatus


def test_should_create_user() -> None:
    """
    Should create a user with default values.
    """

    user = User(
        name="Daniel Cunha",
        email="daniel@email.com",
        password_hash="hash",
    )

    assert user.name == "Daniel Cunha"
    assert user.email == "daniel@email.com"
    assert user.password_hash == "hash"

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
        email="daniel@email.com",
        password_hash="hash",
    )

    user.verify_email()

    assert user.email_verified is True


def test_should_register_login() -> None:
    """
    Should update last login timestamp.
    """

    user = User(
        name="Daniel",
        email="daniel@email.com",
        password_hash="hash",
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
        email="daniel@email.com",
        password_hash="hash",
    )

    user.lock()

    assert user.status == UserStatus.LOCKED


def test_should_disable_user() -> None:
    """
    Should disable the account.
    """

    user = User(
        name="Daniel",
        email="daniel@email.com",
        password_hash="hash",
    )

    user.disable()

    assert user.status == UserStatus.DISABLED


def test_should_activate_user() -> None:
    """
    Should activate the account.
    """

    user = User(
        name="Daniel",
        email="daniel@email.com",
        password_hash="hash",
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
        email="daniel@email.com",
        password_hash="hash",
    )

    assert user.is_active is False


def test_should_be_active_when_email_is_verified() -> None:
    """
    User becomes active after e-mail verification.
    """

    user = User(
        name="Daniel",
        email="daniel@email.com",
        password_hash="hash",
    )

    user.verify_email()

    assert user.is_active is True