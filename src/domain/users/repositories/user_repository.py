from typing import List

from src.infra.orm.entities import User
from src.domain.users.models import CreateUserModel, UserModel

class UserRepository:


    def __init__(self, session_factory):
        self._session_factory = session_factory

    def create_user(self, create_user_model: CreateUserModel) -> UserModel:
        with self._session_factory() as session:
            user_entity = User(**create_user_model.dict())
            session.add(user_entity)
            session.commit()
            session.refresh(user_entity)
            return UserModel.from_orm(user_entity)


    def list_user(self) -> List[UserModel]:
        with self._session_factory() as session:
            users = session.query(User).all()
            return [UserModel.from_orm(user) for user in users]


    def update_user(self, update_user_model: UserModel, id:int) -> UserModel:
        with self._session_factory() as session:
            user_entity = session.query(User).filter(User.id == id).first()
            user_entity.email = update_user_model.email
            user_entity.password = update_user_model.password
            session.add(user_entity)
            session.commit()
            session.refresh(user_entity)

            return UserModel.from_orm(user_entity)


    def delete_user(self, id:int) -> None:
        with self._session_factory() as session:
            user_entity = session.query(User).filter(User.id == id).first()
            session.delete(user_entity)
            session.commit()
            return {"Usuario deletado com sucesso"}


    def get_by_email(self, email:str) -> UserModel:
        with self._session_factory() as session:
            user_entity = session.query(User).filter(User.email == email).first()
            user_model = UserModel.from_orm(user_entity) if user_entity else None
            return user_model


    def get_by_id(self, id: int) -> UserModel:
        with self._session_factory() as session:
            user_entity = session.query(User).filter(User.id == id).first()
            user_model = UserModel.from_orm(user_entity) if user_entity else None
            return user_model