import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


class TestCourierLogin:

    @pytest.mark.parametrize(
        "login_type, password_type, expected_status",
        [
            # TODO: добавьте минимум 3 набора данных.
            # Должны быть позитивные и негативные сценарии.
            #
            # Например:
            # ("valid", "valid", 200),
            # ("missing", "valid", 400),
            # ("valid", "missing", 400),
            # ("invalid", "valid", 404),
        ],
    )
    def test_courier_login(
        self,
        courier,
        login_type,
        password_type,
        expected_status,
    ):
        # TODO: подготовьте login и password для каждого сценария.
        #
        # Для позитивного сценария используйте данные
        # созданного фикстурой курьера.
        #
        # Для негативных сценариев сформируйте необходимые
        # некорректные или отсутствующие данные.

        login = None
        password = None

        payload = {
            "login": login,
            "password": password,
        }

        # TODO: отправьте POST /api/v1/courier/login.
        response = None

        # TODO: проверьте ожидаемый статус ответа.
        assert response.status_code == expected_status
