from typing import List

from fastapi import APIRouter, Depends, Query

from ..schemas import Room, RoomCreate
from ..services.room import RoomService

router = APIRouter(
    prefix='/room',
    tags=['room'],
)


@router.post('/', response_model=Room)
def create_room(
    room_data: RoomCreate,
    service: RoomService = Depends(),
):
    return service.create(room_data=room_data)


@router.get('/{room_id}', response_model=List[Room])
def get_rooms(
    bed_place: int = Query(None),
    # TODO date ??
    service: RoomService = Depends(),
):
    return service.get_list(bed_place)
