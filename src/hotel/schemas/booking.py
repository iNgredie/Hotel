from datetime import date

from pydantic import BaseModel


class BookingBase(BaseModel):
    date_arrival: date
    date_departure: date
    room_id: int


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass
