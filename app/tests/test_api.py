import pytest
from fastapi.testclient import TestClient
from ..app import app, redis_client
import redis
import os
import json

client = TestClient(app)


def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "pong"


def test_set():  # Test set key
    response = client.post("/set", json={
        "key": "test",
        "val": "test1"
    }
    )
    assert response.status_code == 200
    data = response.json()
    assert data == {"test": "test1"}


def test_get():  # Test  Get Functionality
    client.post("/set", json={
        "key": "testkey",
        "val": "testval"
    }
    )
    response = client.get("/get/testkey")
    assert response.status_code == 200
    data = response.json()
    assert data["value"] == "testval"

    response = client.get("/get/testkkkk")
    assert response.status_code == 404


def test_search():  # Test search
    client.post("/set", json={
        "key": "test",
        "val": "test1"
    }
    )

    client.post("/set", json={
        "key": "testkey",
        "val": "testval"
    }
    )

    response = client.get("/search?prefix=t&suffix=y")
    assert response.status_code == 200
    data = response.json()
    assert data["results"] == ["testkey"]

    response = client.get("/search?prefix=t")
    assert response.status_code == 200
    data = response.json()
    assert data["results"].sort() == ["testkey", "test"].sort()

    response = client.get("/search")
    assert response.status_code == 200
    data = response.json()
    assert data["results"].sort() == ["testkey", "test"].sort()

    response = client.get("/search?suffix=y")
    assert response.status_code == 200
    data = response.json()
    assert data["results"] == ["testkey"]

    response = client.get("/search?suffix=qa")
    assert response.status_code == 200
    data = response.json()
    assert data["results"] == []
