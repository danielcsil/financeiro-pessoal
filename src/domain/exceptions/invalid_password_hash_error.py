from __future__ import annotations

from src.domain.exceptions import DomainException


class InvalidPasswordHashError(DomainException):
    """
    Raised when a password hash is invalid.
    """