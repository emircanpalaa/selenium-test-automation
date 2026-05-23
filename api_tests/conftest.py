import os

import pytest


BASE_URL = "https://reqres.in/api"


@pytest.fixture
def api_headers():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        pytest.skip("Set REQRES_API_KEY to run ReqRes API tests")

    return {
        "x-api-key": api_key
    }
