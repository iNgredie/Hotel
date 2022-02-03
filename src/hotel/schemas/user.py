from pydantic import BaseModel

from ..schemas import Role


class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    role_id: int

    class Config:
        orm_mode = True



