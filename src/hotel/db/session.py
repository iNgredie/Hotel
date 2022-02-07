from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from hotel.settings import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
