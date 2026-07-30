from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.config.settings import settings

engine: Engine = create_engine(
    settings.database_url,
    echo=settings.app_debug,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)