from sqlalchemy import Column, Integer, DECIMAL

from ..db.base_class import Base


class Room(Base):
    id = Column(Integer, primary_key=True, index=True)
    price = Column(DECIMAL(5, 2))
    bed_place = Column(Integer)
