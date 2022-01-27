from decimal import Decimal

from pydantic import BaseModel


class Room(BaseModel):
    id: int
    price: Decimal
    bed_place: int
