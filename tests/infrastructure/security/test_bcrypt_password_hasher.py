from __future__ import annotations

import src.infrastructure.security.bcrypt_password_hasher as hasher_module


class FakeBcrypt:
    def gensalt(self, rounds: int) -> bytes:
        return b"fake-salt"

    def hashpw(self, password_bytes: bytes, salt: bytes) -> bytes:
        return b"fake-hash"

    def checkpw(self, password_bytes: bytes, password_hash_bytes: bytes) -> bool:
        return (
            password_bytes == b"Senha123"
            and password_hash_bytes == b"fake-hash"
        )


def test_should_hash_and_verify_with_bcrypt(monkeypatch):
    monkeypatch.setattr(hasher_module, "bcrypt", FakeBcrypt())

    hasher = hasher_module.BcryptPasswordHasher(rounds=4)

    password_hash = hasher.hash("Senha123")

    assert password_hash == "fake-hash"
    assert hasher.verify("Senha123", password_hash)
    assert not hasher.verify("SenhaErrada", password_hash)


def test_should_use_pbkdf2_fallback_when_bcrypt_is_unavailable(monkeypatch):
    monkeypatch.setattr(hasher_module, "bcrypt", None)

    hasher = hasher_module.BcryptPasswordHasher()

    password_hash = hasher.hash("Senha123")

    assert password_hash.startswith("pbkdf2_sha256$")
    assert hasher.verify("Senha123", password_hash)
    assert not hasher.verify("Senha123", "invalid-hash")
    assert not hasher.verify("Senha123", "other$hash$format")
