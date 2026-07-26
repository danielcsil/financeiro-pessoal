from __future__ import annotations

import bcrypt

from src.domain.services.password_verifier import PasswordVerifier
from src.domain.value_objects.hashed_password import HashedPassword
from src.domain.value_objects.password import Password


class BcryptPasswordVerifier(PasswordVerifier):
    """
    Verifies passwords using bcrypt.
    """

    def verify(
        self,
        password: Password,
        password_hash: HashedPassword,
    ) -> bool:
        return bcrypt.checkpw(
            password.value.encode(),
            password_hash.value.encode(),
        )