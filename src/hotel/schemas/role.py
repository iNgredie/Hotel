import enum

from pydantic import BaseModel


class RoleBase(BaseModel):
    id: int
    role_type: str


class Role(RoleBase):

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass
