import requests

from api_tests.conftest import BASE_URL


def test_update_user(api_headers):

    payload = {
        "name": "Emircan Updated",
        "job": "Senior QA"
    }

    response = requests.put(
        f"{BASE_URL}/users/2",
        headers=api_headers,
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Emircan Updated"
    assert data["job"] == "Senior QA"
    assert "updatedAt" in data
