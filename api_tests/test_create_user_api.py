import requests

from api_tests.conftest import BASE_URL


def test_create_user(api_headers):

    payload = {
        "name": "Emircan",
        "job": "QA Automation"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        headers=api_headers,
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Emircan"
    assert data["job"] == "QA Automation"
    assert "id" in data
    assert "createdAt" in data
