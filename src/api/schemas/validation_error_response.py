from pydantic import BaseModel


class ValidationErrorItem(BaseModel):
    field: str
    message: str


class ValidationErrorResponse(BaseModel):
    error: str
    message: str
    details: list[ValidationErrorItem]