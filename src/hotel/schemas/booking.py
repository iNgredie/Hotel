from datetime import datetime

from pydantic import BaseModel


class BookingBase(BaseModel):
    date_arrival: datetime
    date_departure: datetime
    room_id: int


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass
