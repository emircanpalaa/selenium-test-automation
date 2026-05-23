import requests

from api_tests.conftest import BASE_URL


def test_get_user(api_headers):
    response = requests.get(
        f"{BASE_URL}/users/2",
        headers=api_headers,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"
