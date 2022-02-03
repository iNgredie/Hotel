from decimal import Decimal

from pydantic import BaseModel


class RoomBase(BaseModel):
    price: Decimal
    bed_place: int


class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True


class RoomCreate(RoomBase):
    pass


class RoomUpdate(RoomBase):
    pass
