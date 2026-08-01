from __future__ import annotations

"""
SQLAlchemy Session Factory.

===============================================================================
Purpose
===============================================================================

Centralizes the creation and lifecycle management of SQLAlchemy sessions.

A SQLAlchemy Session represents a persistence context responsible for tracking
changes performed during a database interaction.

This module provides a single place responsible for configuring sessions,
ensuring every component of the application uses the same behavior.

===============================================================================
Architecture
===============================================================================

                    SQLAlchemy Engine
                            │
                            ▼
                     SessionFactory
                    ╱               ╲
                   ▼                 ▼
        UnitOfWork            FastAPI Dependency
                   ╲               ╱
                    ▼             ▼
                 SQLAlchemy Session

===============================================================================
Responsibilities
===============================================================================

This module is responsible for:

    • configuring the SQLAlchemy SessionFactory;

    • creating database sessions;

    • providing context managers for scripts;

    • exposing a FastAPI dependency when direct sessions are required.

===============================================================================
Design Principles
===============================================================================

• Single SessionFactory for the application.

• Sessions are short-lived.

• Sessions are never shared between requests.

• Transaction boundaries belong to the UnitOfWork.

===============================================================================
Important
===============================================================================

Application use cases should NEVER receive SQLAlchemy Session objects directly.

Business operations must always execute through UnitOfWork, ensuring proper
transaction management and repository coordination.

The utilities provided here exist primarily for:

    • infrastructure code;

    • administrative scripts;

    • database migrations;

    • testing.
"""

from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.database import engine

# ============================================================================
# Session Factory
# ============================================================================

SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# ============================================================================
# Context Manager
# ============================================================================


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    """
    Creates a transactional SQLAlchemy session.

    This helper is intended for infrastructure code, administrative scripts and
    tests.

    The transaction is automatically committed if no exception occurs.
    Otherwise, the transaction is rolled back before the exception is
    propagated.

    Example
    -------
        with session_scope() as session:
            repository = SqlAlchemyUserRepository(session)
            ...
    """

    session: Session = SessionFactory()

    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


# ============================================================================
# FastAPI Dependency
# ============================================================================


def get_session() -> Generator[Session, None, None]:
    """
    Provides a SQLAlchemy session for FastAPI dependencies.

    This dependency should be used only when direct access to the session is
    required by infrastructure components.

    Application use cases should instead depend on UnitOfWork.

    Example
    -------
        @router.get("/")
        def endpoint(
            session: Session = Depends(get_session),
        ):
            ...
    """

    session: Session = SessionFactory()

    try:
        yield session

    finally:
        session.close()