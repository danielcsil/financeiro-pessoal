from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status

from src.api.schemas.validation_error_response import (
    ValidationErrorItem,
    ValidationErrorResponse,
)

def register_validation_exception_handler(
    app: FastAPI,
) -> None:

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):

        details = []

        for error in exc.errors():

            location = ".".join(
                str(value)
                for value in error["loc"]
                if value != "body"
            )

            details.append(
                ValidationErrorItem(
                    field=location,
                    message=error["msg"],
                )
            )

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ValidationErrorResponse(
                error="VALIDATION_ERROR",
                message="Validation failed",
                details=details,
            ).model_dump(),
        )
