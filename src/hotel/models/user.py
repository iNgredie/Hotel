from sqlalchemy import Column, ForeignKey, Integer, String, Text

from ..db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=255), unique=True)
    username = Column(String(length=255), unique=True)
    password_hash = Column(Text)

    role_id = Column(
        Integer, ForeignKey('role.id', name='fk_user_role_role_id', ondelete='CASCADE'),
    )