from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class LoginResponse:
    id: UUID
    name: str
    email: str
    access_token: str
    authenticated_at: datetime