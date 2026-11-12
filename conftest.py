import os
import uuid

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def courier():
    courier_data = {
        "login": f"courier_{uuid.uuid4().hex}",
        "password": "1234",
        "firstName": "Test",
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=courier_data,
        timeout=60,
    )
    assert response.status_code == 201, response.text

    login_response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": courier_data["login"],
            "password": courier_data["password"],
        },
        timeout=60,
    )
    assert login_response.status_code == 200, login_response.text
    courier_id = login_response.json()["id"]

    try:
        yield {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "id": courier_id,
        }
    finally:
        delete_response = requests.delete(
            f"{BASE_URL}/api/v1/courier/{courier_id}",
            timeout=60,
        )
        assert delete_response.status_code == 200, delete_response.text