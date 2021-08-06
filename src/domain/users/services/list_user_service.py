from typing import List

from src.domain.users.repositories import UserRepository
from src.domain.users.models import UserModel
from src.config.database import db


class ListUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def list_user(self) -> List[UserModel]:
        return self._list_user()

    def _list_user(self) -> List[UserModel]:
        return self._repository.list_user()
