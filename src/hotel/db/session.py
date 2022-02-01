from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ..settings import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
