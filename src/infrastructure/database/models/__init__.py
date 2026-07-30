"""
Modelos ORM da aplicação.

Todos os modelos persistentes devem ser importados neste pacote para que
o SQLAlchemy e o Alembic consigam descobrir automaticamente os metadados.

Exemplo:

    from .user_model import UserModel
    from .account_model import AccountModel
"""

from .base_model import BaseModel

__all__ = [
    "BaseModel",
]