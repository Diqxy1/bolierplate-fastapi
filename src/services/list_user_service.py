from typing import List

from src.repositories.user_repository import UserRepository
from src.models.user_models import UserModel
from src.config.database import db


class ListUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def list_user(self) -> List[UserModel]:
        return self._list_user()

    def _list_user(self) -> List[UserModel]:
        return self._repository.list_user()