from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RegisterUserRequest:
    """
    Input data required to register a new user.
    """

    name: str
    email: str
    password: str
    confirm_password: str
    accepted_terms: bool