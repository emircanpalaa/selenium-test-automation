import requests

from api_tests.conftest import BASE_URL


def test_login_success(api_headers):

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        headers=api_headers,
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert data["token"] is not None


def test_login_invalid(api_headers):

    payload = {
        "email": "emircan_pala@hotmail.com"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        headers=api_headers,
        json=payload,
        timeout=10
    )

    assert response.status_code == 400

    data = response.json()

    assert "error" in data
    assert data["error"] == "Missing password"
