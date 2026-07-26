from pydantic import BaseModel, ConfigDict


class LoginRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    email: str
    password: str