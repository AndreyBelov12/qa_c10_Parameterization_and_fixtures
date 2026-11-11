import os
import uuid

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


class TestCourierLogin:
    @pytest.mark.parametrize(
        "login_type, password_type, expected_status, expected_message",
        [
            ("valid", "valid", 200, None),
            ("missing", "valid", 400, "Недостаточно данных для входа"),
            ("valid", "missing", 400, "Недостаточно данных для входа"),
            ("invalid", "invalid", 404, "Учетная запись не найдена"),
        ],
        ids=[
            "successful_login",
            "missing_login",
            "missing_password",
            "nonexistent_credentials",
        ],
    )
    def test_courier_login(
        self,
        courier,
        login_type,
        password_type,
        expected_status,
        expected_message,
    ):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
        }

        if login_type == "missing":
            payload.pop("login")
        elif login_type == "invalid":
            payload["login"] = f"unknown_{uuid.uuid4().hex}"

        if password_type == "missing":
            payload.pop("password")
        elif password_type == "invalid":
            payload["password"] = uuid.uuid4().hex

        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json=payload,
            timeout=60,
        )

        assert response.status_code == expected_status, response.text

        body = response.json()

        if expected_status == 200:
            assert "id" in body, body
            assert body["id"] == courier["id"], body
        else:
            assert body.get("message") == expected_message, body