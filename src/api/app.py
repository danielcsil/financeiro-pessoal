from __future__ import annotations

from apps.api import app

"""
Personal Finance REST API.

===============================================================================
Purpose
===============================================================================

This module represents the application's Composition Root.

Its responsibility is assembling every component required by the REST API,
including:

    • FastAPI application configuration;

    • OpenAPI metadata;

    • routers;

    • exception handlers.

The Composition Root is the only place where infrastructure components are
wired together. Business rules must never be implemented here.

===============================================================================
Architecture
===============================================================================

                    FastAPI

                        │

        ┌───────────────┴────────────────┐

        ▼                                ▼

   Routers                    Exception Handlers

        │

        ▼

 Application Layer

        ▼

 Domain Layer

===============================================================================
Current Modules
===============================================================================

• Health Check

• Authentication

• Financial Accounts

Future versions will also include:

• Transactions

• Credit Cards

• Investments

• Financial Planning

• Financial Goals

• Reports

• AI Financial Assistant
"""

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.api.exception_handlers.domain import (
    register_domain_exception_handlers,
)
from src.api.exception_handlers.validation import (
    register_validation_exception_handler,
)
from src.api.routers.auth import (
    router as auth_router,
)
from src.api.routers.financial_accounts import (
    router as financial_accounts_router,
)
from src.api.routers.health import (
    router as health_router,
)

# ============================================================================
# Constants
# ============================================================================

API_PREFIX = "/api"

API_TITLE = "Personal Finance API"

API_VERSION = "1.0.0"


def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI application.

    Responsibilities
    ----------------
    • Configure OpenAPI metadata.

    • Register routers.

    • Register exception handlers.

    Returns
    -------
    FastAPI

        Fully configured application.
    """

    app = FastAPI(
        title=API_TITLE,
        version=API_VERSION,
        description="""
Personal Finance is a platform designed to help individuals and families
organize their finances, monitor cash flow and make better financial
decisions.

The API follows the principles of Clean Architecture and exposes the
application's business capabilities through REST endpoints.
""",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # ============================================================================
    # CORS
    # ============================================================================

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # ========================================================================
    # Routers
    # ========================================================================

    app.include_router(
        health_router,
    )

    app.include_router(
        auth_router,
        prefix=API_PREFIX,
    )

    app.include_router(
        financial_accounts_router,
        prefix=API_PREFIX,
    )

    # ========================================================================
    # Exception Handlers
    # ========================================================================

    register_domain_exception_handlers(
        app,
    )

    register_validation_exception_handler(
        app,
    )

    return app


# ============================================================================
# Application
# ============================================================================

app = create_app()