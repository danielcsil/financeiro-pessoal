from __future__ import annotations

"""
Database Configuration.

===============================================================================
Purpose
===============================================================================

Creates and configures the SQLAlchemy Engine used by the application.

The Engine is responsible for managing the connection pool and all
communication with the relational database.

This module is intentionally small because every other database-related
component depends on it.

===============================================================================
Architecture
===============================================================================

                 Application Settings
                         │
                         ▼
                   Database URL
                         │
                         ▼
                SQLAlchemy Engine
                         │
                         ▼
                  SessionFactory
                         │
                         ▼
                 SQLAlchemy Session

===============================================================================
Responsibilities
===============================================================================

This module is responsible for:

    • creating the SQLAlchemy Engine;

    • configuring connection pooling;

    • exposing the application's SessionFactory.

No business logic should ever be implemented here.

===============================================================================
Design Principles
===============================================================================

• One Engine per application.

• One SessionFactory per application.

• Thread-safe.

• Infrastructure concern only.
"""

from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.settings import settings

# ============================================================================
# SQLAlchemy Engine
# ============================================================================

engine: Engine = create_engine(
    settings.database_url,
    echo=settings.app_debug,
    pool_pre_ping=True,
    future=True,
)

# ============================================================================
# Session Factory
# ============================================================================

SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)