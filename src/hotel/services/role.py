from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status


from .. import models
from .. import schemas
from ..db.session import get_session

#
# class RoleService:
#     def __init__(self, session: Session = Depends(get_session)):
#         self.session = session
#
#     def create(
#         self, role_type: str, role_data: schemas.RoleCreate
#     ) -> models.Role:
#         if role_type == RoleType.ADMIN:
#             role = models.Role(**role_data.dict())
#             self.session.add(role)
#             self.session.commit()
#             return role
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
