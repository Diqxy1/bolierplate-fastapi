from src.domain.users.repositories import UserRepository
from src.config.database import db
from src.domain.users.models import CreateUserModel, UserModel

class UpdateUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def update_user(self, update_user_model: CreateUserModel, id: int) -> UserModel:
        return self._update_user(update_user_model, id)

    def _update_user(self, update_user_model: CreateUserModel, id: int) -> UserModel:
        user_update = self._repository.update_user(update_user_model, id)
        return user_update
