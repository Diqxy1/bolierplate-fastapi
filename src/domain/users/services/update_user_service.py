from src.domain.users.repositories import UserRepository
from src.config.database import db
from src.domain.users.models import CreateUserModel, UserModel
from src.shared.exceptions import (
    NotFoundException,
    BadRequestException
)

class UpdateUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def update_user(self, update_user_model: CreateUserModel, id: int) -> UserModel:
        return self._update_user(update_user_model, id)

    def _update_user(self, update_user_model: CreateUserModel, id: int) -> UserModel:
        user_exist = self._repository.get_by_id(id)
        if not user_exist:
            raise NotFoundException(message='Usuário não encontrado')
        user_email_exist = self._repository.get_by_email(update_user_model.email)
        if user_email_exist:
            raise BadRequestException(message='E-email já está em uso')
        user_update = self._repository.update_user(update_user_model, id)
        return user_update
