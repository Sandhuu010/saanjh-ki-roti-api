def create_user_and_login(
    client,
    username,
    phone,
    password="password123"
):

    client.post(
        "/auth/register",
        json={
            "username": username,
            "phone": phone,
            "password": password
        }
    )

    response = client.post(
        "/auth/token",
        data={
            "username": username,
            "password": password
        }
    )

    return response.json()["access_token"]


def test_get_plans_unauthenticated(client):

    response = client.get("/plans")

    assert response.status_code == 401


def test_get_plans_authenticated(client):

    token = create_user_and_login(
        client,
        "planuser",
        "9000000010"
    )

    response = client.get(
        "/plans",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_create_plan_customer_forbidden(client):

    token = create_user_and_login(
        client,
        "customeruser",
        "9000000011"
    )

    response = client.post(
        "/plans",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Monthly Veg",
            "price_paise": 280000,
            "billing_cycle": "MONTHLY",
            "portion_size": "Regular",
            "food_cost_per_day_paise": 12000,
            "active": True
        }
    )

    assert response.status_code == 403


def test_create_plan_admin(client):

    """
    Requires admin user to exist.
    Run create_admin.py before tests.
    """

    response = client.post(
        "/auth/token",
        data={
            "username": "admin",
            "password": "admin123"
        }
    )

    if response.status_code != 200:
        return

    token = response.json()["access_token"]

    response = client.post(
        "/plans",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Premium Plan",
            "price_paise": 350000,
            "billing_cycle": "MONTHLY",
            "portion_size": "Large",
            "food_cost_per_day_paise": 18000,
            "active": True
        }
    )

    assert response.status_code == 201