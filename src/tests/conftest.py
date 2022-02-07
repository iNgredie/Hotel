from typing import Generator

import pytest
from fastapi.testclient import TestClient
from hotel.app import app
from hotel.db.session import SessionLocal


@pytest.fixture(scope='session')
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app) as c:
        yield c

