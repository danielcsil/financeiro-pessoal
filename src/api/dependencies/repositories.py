from functools import lru_cache

from src.infrastructure.persistence.memory.in_memory_user_repository import (
    InMemoryUserRepository,
)


@lru_cache
def get_user_repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()
