from fastapi import Depends
from sqlalchemy.orm import Session


from .. import models
from .. import schemas
from ..db.session import get_session


class RoleService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(
        self, role_data: schemas.RoleCreate
    ) -> models.Role:
        role = models.Role(**role_data.dict())
        self.session.add(role)
        self.session.commit()
        return role
