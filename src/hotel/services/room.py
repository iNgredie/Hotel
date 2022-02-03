from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..db.session import get_session


class RoomService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, room_id: int) -> models.Room:
        room = (
            self.session.query(models.Room)
            .filter_by(
                id=room_id,
            )
            .first()
        )
        if not room:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return room

    def get_list(self, bed_place: int = None) -> List[models.Room]:
        if bed_place:
            query = (
                self.session.query(models.Room)
                .filter(models.Room.bed_place == bed_place)
            )
            return query.all()
        query = self.session.query(models.Room)
        return query.all()

    def create(self, room_data: schemas.RoomCreate) -> models.Room:
        room = models.Room(**room_data.dict())
        self.session.add(room)
        self.session.commit()
        return room

    def update(
        self, room_id: int, room_data: schemas.RoomCreate
    ) -> models.Room:
        room = self._get(room_id)
        for field, value in room_data:
            setattr(room, field, value)
        self.session.commit()
        return room
