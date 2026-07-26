from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum
from uuid import UUID, uuid4
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import HashedPassword


class UserStatus(Enum):
    """
    Represents the lifecycle status of a user account.
    """

    ACTIVE = "active"
    LOCKED = "locked"
    DISABLED = "disabled"


@dataclass(slots=True)
class User:
    """
    Represents a system user.

    This entity is independent of infrastructure concerns such as
    persistence, authentication frameworks or web APIs.
    """

    name: str
    email: Email
    password: HashedPassword

    id: UUID = field(default_factory=uuid4)
    status: UserStatus = UserStatus.ACTIVE

    email_verified: bool = False

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    last_login_at: datetime | None = None

    def activate(self) -> None:
        """
        Activates the user account.
        """
        self.status = UserStatus.ACTIVE
        self.touch()

    def lock(self) -> None:
        """
        Locks the user account.
        """
        self.status = UserStatus.LOCKED
        self.touch()

    def disable(self) -> None:
        """
        Disables the user account.
        """
        self.status = UserStatus.DISABLED
        self.touch()

    def verify_email(self) -> None:
        """
        Marks the e-mail address as verified.
        """
        self.email_verified = True
        self.touch()

    def register_login(self) -> None:
        """
        Stores the instant of the latest successful login.
        """
        self.last_login_at = datetime.now(UTC)
        self.touch()

    def touch(self) -> None:
        """
        Updates the modification timestamp.
        """
        self.updated_at = datetime.now(UTC)

    @property
    def is_active(self) -> bool:
        """
        Indicates whether the account can authenticate.
        """
        return (
            self.status == UserStatus.ACTIVE
            and self.email_verified
        )