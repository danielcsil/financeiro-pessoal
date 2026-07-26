from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status

from src.api.dependencies.services import get_token_verifier
from src.api.dependencies.use_cases import get_current_user_use_case
from src.application.dto.auth.current_user_response import CurrentUserResponse
from src.application.use_cases.auth.get_current_user import (
    GetCurrentUserUseCase,
)
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.services.token_verifier import TokenVerifier

from src.application.dto.auth.current_user_response import (
    CurrentUserResponse,
)

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    token_verifier: TokenVerifier = Depends(get_token_verifier),
    use_case: GetCurrentUserUseCase = Depends(get_current_user_use_case),
) -> CurrentUserResponse:
    if credentials is None:
        raise InvalidCredentialsError()

    claims = token_verifier.verify_access_token(
        credentials.credentials,
    )

    return use_case.execute(claims.user_id)