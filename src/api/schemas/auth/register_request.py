from pydantic import BaseModel, ConfigDict


class RegisterRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    name: str
    email: str
    password: str
    password_confirmation: str
    accept_terms: bool