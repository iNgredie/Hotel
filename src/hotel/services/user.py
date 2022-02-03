from fastapi import Depends, HTTPException, status
from passlib.handlers.bcrypt import bcrypt
from sqlalchemy import or_
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..db.session import get_session


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    def register_new_user(self, user_data: schemas.UserCreate) -> models.User:
        user_exist = (
            self.session.query(models.User)
                .filter(
                or_(
                    models.User.username == user_data.username,
                    models.User.email == user_data.email,
                )
            )
            .first()
        )
        if user_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email or username already exists',
            )
        role = (
            self.session.query(models.Role)
                .filter_by(
                role_type='manager',
            )
            .first()
        )
        user = models.User(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
            role_id=role.id,
        )

        self.session.add(user)
        self.session.commit()

        return user

    def authenticate_user(self, username: str, password: str):
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
        )

        user = (
            self.session
            .query(models.User)
            .filter(models.User.username == username)
            .first()
        )

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception
