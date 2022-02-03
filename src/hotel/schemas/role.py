from pydantic import BaseModel


class RoleBase(BaseModel):
    role_type: str


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass
