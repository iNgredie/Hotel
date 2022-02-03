from fastapi import APIRouter, Depends

from ..schemas import Booking, BookingCreate
from ..services.booking import BookingService

router = APIRouter(
    prefix='/booking',
    tags=['booking']
)


@router.post('/', response_model=Booking)
def create_booking(
    booking_data: BookingCreate,
    service: BookingService = Depends(),
):
    return service.create(booking_data=booking_data)


@router.get('/{booking_id}', response_model=Booking)
def get_booking(
    booking_id: int,
    service: BookingService = Depends(),
):
    return service.get(booking_id=booking_id)


@router.delete('/{booking_id}', response_model=Booking)
def remove_booking(
    booking_id: int,
    service: BookingService = Depends(),
):
    return service.remove_booking(booking_id=booking_id)
