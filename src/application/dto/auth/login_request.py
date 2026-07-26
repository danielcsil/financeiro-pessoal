from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LoginRequest:
    """
    Request for user authentication.
    """

    email: str
    password: str