from fastapi import APIRouter, Depends

from ..schemas import Role, RoleCreate
from ..services.role import RoleService

router = APIRouter(
    prefix='/role',
    tags=['role']
)


@router.post('/', response_model=Role)
def create_role(
    role_data: RoleCreate,
    service: RoleService = Depends(),
):
    return service.create(role_data=role_data)
