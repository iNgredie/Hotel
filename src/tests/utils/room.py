from decimal import Decimal

from sqlalchemy.orm import Session

from hotel import models
from hotel.schemas import RoomCreate
from hotel.services.room import RoomService
from tests.utils.utils import random_number


def create_random_room(db: Session) -> models.Room:
    price = Decimal(random_number())
    bed_place = random_number()
    room_data = RoomCreate(price=price, bed_place=bed_place)
    service = RoomService(db)
    return service.create(room_data=room_data)


