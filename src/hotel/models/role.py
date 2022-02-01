from sqlalchemy import Column, Integer, String

from ..db.base_class import Base


class Role(Base):
    id = Column(Integer, primary_key=True, index=True)
    role_type = Column(String(length=255), unique=True)
