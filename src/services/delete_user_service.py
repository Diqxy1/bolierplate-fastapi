from src.repositories.user_repository  import UserRepository
from src.config.database import db

class DeleteUserService:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)
    
    def delete(self, id:int) -> None:
        return self._delete(id)

    def _delete(self, id:int) -> None:
        delete_user = self._repository.delete_user(id)
        return delete_user