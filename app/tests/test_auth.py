def test_register_user_success(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser1",
            "phone": "9000000001",
            "password": "password123"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "testuser1"
    assert "password_hash" not in data


def test_register_duplicate_username(client):

    payload = {
        "username": "duplicate_user",
        "phone": "9000000002",
        "password": "password123"
    }

    client.post("/auth/register", json=payload)

    response = client.post(
        "/auth/register",
        json={
            "username": "duplicate_user",
            "phone": "9000000003",
            "password": "password123"
        }
    )

    assert response.status_code == 409


def test_register_duplicate_phone(client):

    payload = {
        "username": "phone_user1",
        "phone": "9000000004",
        "password": "password123"
    }

    client.post("/auth/register", json=payload)

    response = client.post(
        "/auth/register",
        json={
            "username": "phone_user2",
            "phone": "9000000004",
            "password": "password123"
        }
    )

    assert response.status_code == 409


def test_login_success(client):

    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "phone": "9000000005",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/token",
        data={
            "username": "loginuser",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client):

    response = client.post(
        "/auth/token",
        data={
            "username": "fakeuser",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401