from fastapi import APIRouter
from typing import List

from src.domain.users.models import UserModel, CreateUserModel
from src.domain.users.services import (
    CreateUserService,
    ListUserService,
    UpdateUserService,
    DeleteUserService,
    DetailUserService
)


router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.get('/', response_model=List[UserModel])
def list_users():
    service = ListUserService()
    return service.list_user()


@router.post('/', response_model=UserModel)
def create_user(create_user_model: CreateUserModel):
    service = CreateUserService()
    return service.create(create_user_model)

@router.put('/{id}', response_model=CreateUserModel)
def update_user(update_user_model: CreateUserModel, id: int):
    service = UpdateUserService()
    return service.update_user(update_user_model, id)

@router.delete('/{id}', response_model=None)
def delete_user(id:int):
    service = DeleteUserService()
    return service.delete(id)

@router.get('/{id}', response_model=UserModel)
def detail_user(id: int):
    service = DetailUserService()
    return service.detail_user(id)
