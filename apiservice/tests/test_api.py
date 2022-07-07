from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)


def test_ping():
    response = client.get("/")
    assert response.status_code == 200


def test_get():
    response = client.get("/get/aa")
    assert response.status_code == 500


def test_set():
    pass


def test_search():
    pass
