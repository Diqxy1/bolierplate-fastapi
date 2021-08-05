from src.repositories.user_repository import UserRepository
from src.config.database import db
from src.models.user_models import UserModel, CreateUserModel

class CreateUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def create(self, create_user_model= CreateUserModel) -> UserModel:
        return self._create(create_user_model)

    def _create(self, create_user_model = CreateUserModel) -> UserModel:
        user_created = self._repository.create_user(create_user_model)
        return user_created