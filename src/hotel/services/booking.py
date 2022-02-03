from datetime import date, timedelta

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from hotel import models
from hotel import schemas
from hotel.db.session import get_session


class BookingService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, booking_id: int):
        booking = (
            self.session.query(models.Booking)
            .filter_by(
                id=booking_id,
            )
            .first()
        )
        if not booking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return booking

    def get(self, booking_id: int):
        return self._get(booking_id)

    def create(
        self, booking_data: schemas.BookingCreate
    ) -> models.Booking:
        booking = models.Booking(**booking_data.dict())
        self.session.add(booking)
        self.session.commit()
        return booking

    def remove_booking(self, booking_id: int):
        booking = self._get(booking_id)
        today = date.today()
        if booking.date_arrival - timedelta(days=3) < today:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Can not cancel the booking, less than three days'
            )
        self.session.delete(booking)
        self.session.commit()
