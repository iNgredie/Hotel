from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .. import schemas
from ..services.user import UserService

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/sign-up', response_model=schemas.User)
def sign_up(
    user_data: schemas.UserCreate,
    service: UserService = Depends(),
):
    return service.register_new_user(user_data)


@router.post('/sing-in', response_model=schemas.User)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(),
):
    return service.authenticate_user(
        form_data.username,
        form_data.password,
    )

#
# @router.get('/user', response_model=models.User)
# def get_user(user: schemas.User = Depends(get_current_user)):
#     return user
