import os

import pytest
import requests


BASE_URL = "https://yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN")


@pytest.fixture
def api_headers():
    if not TOKEN:
        pytest.fail(
            "Не задана переменная окружения YOUGILE_TOKEN"
        )

    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }


@pytest.fixture
def create_project(api_headers):
    data = {
        "title": "Test project for API"
    }

    response = requests.post(
        f"{BASE_URL}/projects",
        headers=api_headers,
        json=data,
    )

    assert response.status_code == 201

    return response.json()["id"]
