from src.domain.users.repositories import UserRepository
from src.domain.users.models import UserModel
from src.config.database import db
from src.shared.exceptions import NotFoundException


class DetailUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def detail_user(self, id:int) -> UserModel:
        user = self._detail_user(id)
        return user

    def _detail_user(self, id:int) -> UserModel:
        user_exist = self._repository.get_by_id(id)
        if not user_exist:
            raise NotFoundException(message='Usuário não encontrado')
        return user_exist
