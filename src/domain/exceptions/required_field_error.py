from __future__ import annotations

from src.domain.exceptions import DomainException


class RequiredFieldError(DomainException):
    """
    Raised when a required field is not provided.
    """