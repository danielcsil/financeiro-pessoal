from __future__ import annotations

"""
Alembic environment configuration.

Este módulo integra o Alembic à infraestrutura da aplicação,
utilizando a mesma configuração de banco de dados definida em
Settings e o mesmo Engine utilizado pela API.

Todas as migrações devem ser geradas a partir do metadata
registrado na classe Base.
"""

from logging.config import fileConfig

from alembic import context

from src.config.settings import settings
from src.infrastructure.database.base import Base
from src.infrastructure.database.database import engine

# ============================================================================
# IMPORTAÇÃO DOS MODELOS
# ============================================================================
# Todos os modelos ORM devem ser importados aqui para que sejam registrados
# no Base.metadata e possam ser detectados pelo Alembic.
#
# Conforme o projeto crescer, recomenda-se substituir estes imports por:
#
#     from src.infrastructure.database import models
#
# onde models/__init__.py importa todos os modelos do projeto.
# ============================================================================

from src.infrastructure.database.models.user_model import UserModel
from src.infrastructure.database.models.financial_account_model import (
    FinancialAccountModel,
)

# Configuração do Alembic
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Garante que o Alembic utilize a mesma URL da aplicação.
config.set_main_option(
    "sqlalchemy.url",
    settings.database_url,
)

# Metadata utilizado para autogenerate.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Executa migrations em modo offline.
    """

    context.configure(
        url=settings.database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={
            "paramstyle": "named",
        },
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Executa migrations utilizando a mesma Engine da aplicação.
    """

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
            render_as_batch=False,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()