from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.api.schemas.error_response import ErrorResponse

from src.domain.exceptions.domain_exception import DomainException
from src.domain.exceptions.email_already_exists_error import (
    EmailAlreadyExistsError,
)
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.exceptions.invalid_email_error import (
    InvalidEmailError,
)
from src.domain.exceptions.password_mismatch_error import (
    PasswordMismatchError,
)
from src.domain.exceptions.terms_not_accepted_error import (
    TermsNotAcceptedError,
)

def register_domain_exception_handlers(
    app: FastAPI,
) -> None:

    @app.exception_handler(EmailAlreadyExistsError)
    async def email_exists(
        request: Request,
        exc: EmailAlreadyExistsError,
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=ErrorResponse(
                error="EMAIL_ALREADY_EXISTS",
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(InvalidCredentialsError)
    async def invalid_credentials(
        request: Request,
        exc: InvalidCredentialsError,
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=ErrorResponse(
                error="INVALID_CREDENTIALS",
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(PasswordMismatchError)
    async def password_mismatch(
        request: Request,
        exc: PasswordMismatchError,
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=ErrorResponse(
                error="PASSWORD_MISMATCH",
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(TermsNotAcceptedError)
    async def terms_not_accepted(
        request: Request,
        exc: TermsNotAcceptedError,
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=ErrorResponse(
                error="TERMS_NOT_ACCEPTED",
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(InvalidEmailError)
    async def invalid_email(
        request: Request,
        exc: InvalidEmailError,
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=ErrorResponse(
                error="INVALID_EMAIL",
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(DomainException)
    async def domain_exception(
        request: Request,
        exc: DomainException,
    ):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=ErrorResponse(
                error="DOMAIN_ERROR",
                message=str(exc),
            ).model_dump(),
        )