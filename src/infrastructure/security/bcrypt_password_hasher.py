from __future__ import annotations

import base64
import hashlib
import hmac
import secrets

try:
    import bcrypt
except ModuleNotFoundError:  # pragma: no cover - fallback for local test envs
    bcrypt = None

from src.domain.services.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
    """
    PasswordHasher implementation based on bcrypt.
    """

    def __init__(self, rounds: int = 12) -> None:
        self._rounds = rounds

    def hash(self, password: str) -> str:
        """
        Generates a password hash for the given password.
        """

        if bcrypt is None:
            salt = secrets.token_bytes(16)
            digest = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt,
                120_000,
            )
            encoded_salt = base64.b64encode(salt).decode("ascii")
            encoded_digest = base64.b64encode(digest).decode("ascii")
            return f"pbkdf2_sha256${encoded_salt}${encoded_digest}"

        password_bytes = password.encode("utf-8")

        salt = bcrypt.gensalt(rounds=self._rounds)

        password_hash = bcrypt.hashpw(
            password_bytes,
            salt,
        )

        return password_hash.decode("utf-8")

    def verify(
        self,
        password: str,
        password_hash: str,
    ) -> bool:
        """
        Verifies whether a password matches the stored hash.
        """

        if bcrypt is None:
            try:
                algorithm, encoded_salt, encoded_digest = password_hash.split(
                    "$",
                    2,
                )
            except ValueError:
                return False

            if algorithm != "pbkdf2_sha256":
                return False

            salt = base64.b64decode(encoded_salt)
            expected_digest = base64.b64decode(encoded_digest)
            actual_digest = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt,
                120_000,
            )
            return hmac.compare_digest(actual_digest, expected_digest)

        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8"),
        )
