from __future__ import annotations

from src.domain.exceptions.domain_exception import DomainException


class InvalidCredentialsError(DomainException):
    """
    Raised when the provided authentication credentials are invalid.
    """

    def __init__(self) -> None:
        super().__init__("Invalid credentials.")