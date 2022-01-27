from sqlalchemy import Column, Enum, Integer


from ..db.base_class import Base
from ..schemas import RoleType


class Role(Base):
    id = Column(Integer, primary_key=True, index=True)
    role_type = Column(Enum(RoleType), default=RoleType.MANAGER)
