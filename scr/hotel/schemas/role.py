import enum

from pydantic import BaseModel


class RoleType(str, enum.Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'


class RoleBase(BaseModel):
    id: int
    role_type: RoleType


class Role(RoleBase):

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass
