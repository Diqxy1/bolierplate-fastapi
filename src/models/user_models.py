from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True

class CreateUserModel(BaseModel):
    email: str
    password: str