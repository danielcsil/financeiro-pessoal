from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class LoginResponse(BaseModel):
    id: UUID
    name: str
    email: str
    access_token: str
    authenticated_at: datetime