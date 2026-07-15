from fastapi.testclient import TestClient
from app.main import app, users

client = TestClient(app)

def setup_function():
    users.clear()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI"}

def test_create_user():
    response = client.post(
        "/users",
        json={
            "id": 1,
            "username": "Ali"
        }
    )

    assert response.status_code == 201
    assert response.json()["username"] == "Ali"

def test_get_all_users():
    client.post("/users", json={"id": 1, "username": "Ali"})
    client.post("/users", json={"id": 2, "username": "Bob"})

    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_single_user():
    client.post("/users", json={"id": 1, "username": "Ali"})

    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json()["username"] == "Ali"

def test_user_not_found():
    response = client.get("/users/987")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_update_user():
    client.post("/users", json={"id": 1, "username": "Ali"})

    response = client.put(
        "/users/1",
        json={
            "id": 1,
            "username": "Josie"
        }
    )

    assert response.status_code == 200
    assert response.json()["username"] == "Josie"

def test_update_missing_user():
    response = client.put(
        "/users/10",
        json={
            "id": 10,
            "username": "Nobody"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_delete_user():
    client.post("/users", json={"id": 1, "username": "Ali"})
    response = client.delete("/users/1")

    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"

def test_delete_missing_person():
    response = client.delete("/users/20")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_users_empty():
    response = client.get("/users")

    assert response.status_code == 200
    assert response.json() == []

def test_duplicate_user():
    client.post(
        "/users",
        json={
            "id": 1,
            "username": "Ali"
        }
    )

    response = client.post("/users", json={
            "id": 1,
            "username": "Ali"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"