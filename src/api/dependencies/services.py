from functools import lru_cache

from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)
from src.infrastructure.security.bcrypt_password_verifier import (
    BcryptPasswordVerifier,
)
from src.infrastructure.security.jwt_token_provider import (
    JwtTokenProvider,
)
from src.infrastructure.security.jwt_token_verifier import (
    JwtTokenVerifier,
)


JWT_SECRET = "0123456789abcdef0123456789abcdef"


@lru_cache
def get_password_hasher() -> BcryptPasswordHasher:
    return BcryptPasswordHasher()


@lru_cache
def get_password_verifier() -> BcryptPasswordVerifier:
    return BcryptPasswordVerifier()


@lru_cache
def get_token_provider() -> JwtTokenProvider:
    return JwtTokenProvider(secret_key=JWT_SECRET)


@lru_cache
def get_token_verifier() -> JwtTokenVerifier:
    return JwtTokenVerifier(secret_key=JWT_SECRET)