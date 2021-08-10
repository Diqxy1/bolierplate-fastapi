from dependency_injector import containers, providers

from src.domain.users.repositories import UserRepository
from src.domain.users.services import (
    CreateUserService,
    UpdateUserService,
    ListUserService,
    DeleteUserService,
    DetailUserService
)

class UserContainer(containers.DeclarativeContainer):

    db = providers.Dependency()

    user_repository = providers.Factory(
        UserRepository,
        session_factory = db.provided.session,
    )

    create_user_service = providers.Factory(
        CreateUserService,
        repository=user_repository
    )

    list_user_service = providers.Factory(
        ListUserService,
        repository=user_repository
    )

    update_user_service = providers.Factory(
        UpdateUserService,
        repository=user_repository
    )

    delete_user_service = providers.Factory(
        DeleteUserService,
        repository=user_repository
    )

    detail_user_service = providers.Factory(
        DetailUserService,
        repository=user_repository
    )
