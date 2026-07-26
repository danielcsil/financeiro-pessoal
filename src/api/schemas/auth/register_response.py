from uuid import UUID

from pydantic import BaseModel


class RegisterResponse(BaseModel):
    id: UUID
    name: str
    email: str