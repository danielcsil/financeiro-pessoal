"""
Papéis (roles) disponíveis para os usuários do sistema.

Este enum define os perfis de acesso reconhecidos pelo domínio.
Novos papéis devem ser adicionados aqui para manter consistência
em toda a aplicação.
"""

from __future__ import annotations

from enum import StrEnum


class UserRole(StrEnum):
    """
    Papéis de acesso do usuário.
    """

    USER = "USER"
    ADMIN = "ADMIN"