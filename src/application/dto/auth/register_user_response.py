from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class RegisterUserResponse:
    """
    Represents the result of a successful user registration.
    """

    id: UUID
    name: str
    email: str
    email_verified: bool
    created_at: datetime