from datetime import datetime

from pydantic import BaseModel

from hotel.schemas.room import Room


class BookingBase(BaseModel):
    id: int
    date_arrival: datetime
    date_departure: datetime
    room_id: Room


class Booking(BookingBase):

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass
