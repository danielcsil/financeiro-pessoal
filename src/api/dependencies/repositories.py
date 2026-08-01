from __future__ import annotations

from functools import lru_cache

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.domain.repositories.user_repository import UserRepository

from src.infrastructure.database.session_factory import (
    SessionFactory,
)
from src.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)


def get_session_factory() -> sessionmaker[Session]:
    """
    Returns the application's SessionFactory.
    """

    return SessionFactory


def get_session() -> Session:
    """
    Creates a new database session.

    This helper exists mainly for scripts and tests.
    Application use cases should prefer UnitOfWork.
    """

    return SessionFactory()


@lru_cache
def get_user_repository() -> UserRepository:
    """
    Returns a concrete UserRepository.

    This method exists only for backward compatibility.
    New code should obtain repositories through UnitOfWork.
    """

    return SqlAlchemyUserRepository(
        session=get_session(),
    )
