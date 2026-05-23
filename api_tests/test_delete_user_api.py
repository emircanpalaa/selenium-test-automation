import requests

from api_tests.conftest import BASE_URL


def test_delete_user(api_headers):

    response = requests.delete(
        f"{BASE_URL}/users/2",
        headers=api_headers,
        timeout=10
    )

    assert response.status_code == 204
    assert response.text == ""
