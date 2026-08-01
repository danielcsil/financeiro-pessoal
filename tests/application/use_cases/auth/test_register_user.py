from __future__ import annotations

import pytest

from infrastructure.memory.in_memory_unit_of_work import (
    InMemoryUnitOfWork,
)

from src.application.dto.auth.register_user_request import (
    RegisterUserRequest,
)
from src.application.use_cases.auth.register_user import (
    RegisterUserUseCase,
)
from src.domain.exceptions import (
    EmailAlreadyExistsError,
    InvalidEmailError,
    InvalidPasswordError,
    PasswordMismatchError,
    RequiredFieldError,
    TermsNotAcceptedError,
)
from src.infrastructure.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)


def create_use_case() -> RegisterUserUseCase:
    """
    Creates a RegisterUserUseCase backed by an in-memory Unit of Work.
    """

    return RegisterUserUseCase(
        unit_of_work=InMemoryUnitOfWork(),
        password_hasher=BcryptPasswordHasher(),
    )


def create_request(
    **kwargs,
) -> RegisterUserRequest:

    data = {
        "name": "Daniel Cunha",
        "email": "daniel@email.com",
        "password": "Senha123",
        "confirm_password": "Senha123",
        "accepted_terms": True,
    }

    data.update(kwargs)

    return RegisterUserRequest(**data)


def test_should_register_user_successfully() -> None:
    """
    Should register a new user.
    """

    use_case = create_use_case()

    response = use_case.execute(
        create_request(),
    )

    assert response.name == "Daniel Cunha"
    assert response.email == "daniel@email.com"
    assert response.email_verified is False
    assert response.id is not None
    assert response.created_at is not None


def test_should_not_register_user_with_existing_email() -> None:
    """
    Should reject duplicated e-mails.
    """

    use_case = create_use_case()

    request = create_request()

    use_case.execute(
        request,
    )

    with pytest.raises(
        EmailAlreadyExistsError,
    ):
        use_case.execute(
            request,
        )


def test_should_trim_name() -> None:
    """
    Should remove leading and trailing spaces from name.
    """

    use_case = create_use_case()

    response = use_case.execute(
        create_request(
            name="   Daniel Cunha   ",
        ),
    )

    assert response.name == "Daniel Cunha"


def test_should_normalize_email() -> None:
    """
    Should normalize e-mail before persisting.
    """

    use_case = create_use_case()

    response = use_case.execute(
        create_request(
            email="  Daniel@Email.Com  ",
        ),
    )

    assert response.email == "daniel@email.com"


def test_should_not_register_without_name() -> None:
    """
    Name is mandatory.
    """

    use_case = create_use_case()

    with pytest.raises(
        RequiredFieldError,
    ):
        use_case.execute(
            create_request(
                name="",
            ),
        )


def test_should_not_register_without_email() -> None:
    """
    Email is mandatory.
    """

    use_case = create_use_case()

    with pytest.raises(
        InvalidEmailError,
    ):
        use_case.execute(
            create_request(
                email="",
            ),
        )


def test_should_not_register_without_password() -> None:
    """
    Password is mandatory.
    """

    use_case = create_use_case()

    with pytest.raises(
        InvalidPasswordError,
    ):
        use_case.execute(
            create_request(
                password="",
            ),
        )


def test_should_not_register_when_passwords_do_not_match() -> None:
    """
    Password confirmation must match.
    """

    use_case = create_use_case()

    with pytest.raises(
        PasswordMismatchError,
    ):
        use_case.execute(
            create_request(
                confirm_password="OutraSenha123",
            ),
        )


def test_should_not_register_without_accepting_terms() -> None:
    """
    Terms acceptance is mandatory.
    """

    use_case = create_use_case()

    with pytest.raises(
        TermsNotAcceptedError,
    ):
        use_case.execute(
            create_request(
                accepted_terms=False,
            ),
        )