from __future__ import annotations

from abc import ABC, abstractmethod


class PasswordHasher(ABC):
    """
    Defines the contract responsible for password hashing and
    verification.

    The domain does not depend on any specific cryptographic
    implementation such as bcrypt or Argon2.
    """

    @abstractmethod
    def hash(self, password: str) -> str:
        """
        Returns a secure hash for the provided password.
        """
        raise NotImplementedError

    @abstractmethod
    def verify(
        self,
        password: str,
        password_hash: str,
    ) -> bool:
        """
        Verifies whether the password matches the stored hash.
        """
        raise NotImplementedError