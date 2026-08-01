from __future__ import annotations

"""
Financial Account SQLAlchemy Model.

===============================================================================
Purpose
===============================================================================

Defines the SQLAlchemy ORM model responsible for persisting financial accounts.

This model belongs exclusively to the Infrastructure Layer and represents the
physical database schema used by the application.

Unlike the FinancialAccount domain entity, this class contains persistence
concerns only and must never implement business rules.

===============================================================================
Responsibilities
===============================================================================

The model is responsible for:

    • representing the database table;

    • defining columns and SQL constraints;

    • configuring indexes and relationships;

    • providing metadata required by SQLAlchemy.

Business rules such as validations, state transitions and calculations belong
to the Domain Layer and must never be implemented here.

===============================================================================
Architecture
===============================================================================

                    Domain Layer

                    FinancialAccount
                           │
                           ▼
                FinancialAccountMapper
                           │
                           ▼
                FinancialAccountModel
                           │
                           ▼
                    PostgreSQL Database

The mapper is the single component responsible for converting between the
Domain Entity and the persistence model.

===============================================================================
Design Principles
===============================================================================

• Infrastructure concern only.

• SQLAlchemy specific.

• No business logic.

• No validation logic.

• Represents the physical database schema.

===============================================================================
Persistence Notes
===============================================================================

The current balance is intentionally stored in the database.

Although it is derived from financial transactions, persisting this value
avoids recalculating the balance every time an account is displayed. Future
transaction use cases will be responsible for keeping this value synchronized.
"""

from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.domain.enums.account_type import AccountType
from src.infrastructure.database.base import Base


class FinancialAccountModel(Base):
    """
    SQLAlchemy persistence model representing a financial account.

    Each instance corresponds to a single row in the
    ``financial_accounts`` table.
    """

    __tablename__ = "financial_accounts"

    # -------------------------------------------------------------------------
    # Primary Key
    # -------------------------------------------------------------------------

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    # -------------------------------------------------------------------------
    # Ownership
    # -------------------------------------------------------------------------

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # -------------------------------------------------------------------------
    # General Information
    # -------------------------------------------------------------------------

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    institution: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
    )

    account_type: Mapped[AccountType] = mapped_column(
        Enum(AccountType),
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # Financial Information
    # -------------------------------------------------------------------------

    initial_balance: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        nullable=False,
    )

    current_balance: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        nullable=False,
    )

    # -------------------------------------------------------------------------
    # Presentation
    # -------------------------------------------------------------------------

    color: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="#2563EB",
    )

    icon: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="wallet",
    )

    # -------------------------------------------------------------------------
    # Configuration
    # -------------------------------------------------------------------------

    include_in_cash_flow: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    include_in_net_worth: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    # -------------------------------------------------------------------------
    # Status
    # -------------------------------------------------------------------------

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )

    # -------------------------------------------------------------------------
    # Auditing
    # -------------------------------------------------------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
