from fastapi import APIRouter

from ..schemas import Role, RoleCreate
from ..services.role import RoleService

router = APIRouter(
    prefix='/role',
    tags=['role']
)
