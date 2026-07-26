from __future__ import annotations

from src.domain.exceptions import DomainException


class InvalidPasswordError(DomainException):
    """
    Raised when a password is invalid.
    """