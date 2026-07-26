from __future__ import annotations

from src.domain.value_objects.hashed_password import HashedPassword
from src.domain.value_objects.password import Password
from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)
from src.infrastructure.security.bcrypt_password_verifier import (
    BcryptPasswordVerifier,
)


def test_should_verify_correct_password() -> None:
    hasher = BcryptPasswordHasher()
    verifier = BcryptPasswordVerifier()

    password = Password("Senha123")
    password_hash = HashedPassword(
        hasher.hash(password.value)
    )

    assert verifier.verify(
        password,
        password_hash,
    )


def test_should_reject_invalid_password() -> None:
    hasher = BcryptPasswordHasher()
    verifier = BcryptPasswordVerifier()

    password_hash = HashedPassword(
        hasher.hash("Senha123")
    )

    assert not verifier.verify(
        Password("OutraSenha123"),
        password_hash,
    )