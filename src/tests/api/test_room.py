from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.utils.room import create_random_room


def test_create_room(client: TestClient) -> None:
    data = {'price': 10, 'bed_place': 5}
    response = client.post('room/', json=data)
    assert response.status_code == 200
    content = response.json()
    assert content['price'] == data['price']
    assert content['bed_place'] == data['bed_place']
    assert 'id' in content


def test_read_room(
    client: TestClient, db: Session
) -> None:
    room = create_random_room(db)
    response = client.get(f'room/{room.id}')
    assert response.status_code == 200
