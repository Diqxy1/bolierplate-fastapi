from src.domain.users.repositories import UserRepository
from src.config.database import db
from src.shared.exceptions import NotFoundException

class DeleteUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)

    def delete(self, id:int) -> None:
        return self._delete(id)

    def _delete(self, id:int) -> None:
        user_exist = self._repository.get_by_id(id)
        if not user_exist:
            raise NotFoundException(message='Usuário não encontrado')
        delete_user = self._repository.delete_user(id)
        return delete_user
