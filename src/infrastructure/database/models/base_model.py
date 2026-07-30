from __future__ import annotations

"""
Classe base para todos os modelos ORM.

Esta classe concentra os atributos comuns a todas as entidades
persistidas no banco de dados, reduzindo duplicação e garantindo
consistência entre os modelos.

Nenhuma regra de negócio deve ser implementada aqui.
"""

from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.infrastructure.database.base import Base


class BaseModel(Base):
    """
    Classe base para todos os modelos ORM.

    As entidades concretas herdam desta classe e recebem
    automaticamente os campos comuns.
    """

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )