from __future__ import annotations

"""
Factory responsável pela criação e gerenciamento de sessões do SQLAlchemy.

A sessão representa uma unidade de trabalho (Unit of Work) sobre o banco
de dados. Este módulo centraliza sua criação para evitar duplicação de
configuração em diferentes partes da aplicação.
"""

from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.database import engine


# -----------------------------------------------------------------------------
# Configuração da fábrica de sessões
# -----------------------------------------------------------------------------

SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# -----------------------------------------------------------------------------
# Context Manager
# -----------------------------------------------------------------------------

@contextmanager
def session_scope() -> Generator[Session, None, None]:
    """
    Cria uma sessão do SQLAlchemy.

    Em caso de sucesso, realiza commit.
    Em caso de erro, realiza rollback.

    Exemplo:

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


# -----------------------------------------------------------------------------
# Dependency para FastAPI
# -----------------------------------------------------------------------------

def get_session() -> Generator[Session, None, None]:
    """
    Dependency utilizada pela FastAPI.

    Exemplo:

        @router.get("/")
        def endpoint(
            session: Session = Depends(get_session)
        ):
            ...
    """

    session: Session = SessionFactory()

    try:
        yield session

    finally:
        session.close()