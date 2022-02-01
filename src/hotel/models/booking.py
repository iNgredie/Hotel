from sqlalchemy import Column, Date, ForeignKey, Integer

from ..db.base_class import Base


class Booking(Base):
    id = Column(Integer, primary_key=True, index=True)
    date_arrival = Column(Date())
    date_departure = Column(Date())

    room_id = Column(
        Integer, ForeignKey('room.id', name='fk_booking_room_room_id', ondelete='CASCADE'),
    )
