from __future__ import annotations

from abc import ABC, abstractmethod

from src.domain.value_objects.hashed_password import HashedPassword
from src.domain.value_objects.password import Password


class PasswordVerifier(ABC):
    """
    Service responsible for verifying passwords.
    """

    @abstractmethod
    def verify(
        self,
        password: Password,
        password_hash: HashedPassword,
    ) -> bool:
        """
        Returns True when the password matches the hash.
        """