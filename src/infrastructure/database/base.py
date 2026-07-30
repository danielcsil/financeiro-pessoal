from __future__ import annotations

"""
Define a classe base utilizada por todos os modelos ORM do projeto.

A utilização de uma Base comum permite que o SQLAlchemy conheça todas as
entidades persistentes da aplicação e facilite operações como:

- criação das tabelas;
- geração de migrations pelo Alembic;
- inspeção do metadata;
- relacionamento entre entidades.

Nenhuma regra de negócio deve existir nesta camada.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Classe base para todos os modelos ORM.

    Todas as entidades persistidas em banco devem herdar desta classe.

    Exemplo:

        class UserModel(Base):
            __tablename__ = "users"
            ...
    """

    pass