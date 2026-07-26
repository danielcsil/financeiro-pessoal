from __future__ import annotations

from src.domain.exceptions import DomainException


class EmailAlreadyExistsError(DomainException):
    """
    Raised when trying to register an already existing e-mail.
    """