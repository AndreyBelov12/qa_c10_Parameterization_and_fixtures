import os
import uuid

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def courier():
    # TODO: сгенерируйте уникальный логин курьера.
    # Например, используйте uuid.
    login = f"TODO_{uuid.uuid4().hex[:8]}"

    courier_data = {
        "login": login,
        "password": "1234",
        "firstName": "Test",
    }

    # TODO: создайте курьера через POST /api/v1/courier.
    # Сохраните ответ, чтобы убедиться, что создание прошло успешно.
    response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=courier_data,
    )

    # TODO: получите id созданного курьера.
    # Для этого используйте POST /api/v1/courier/login
    # с login и password из courier_data.
    #
    # login_response = requests.post(...)
    # courier_id = login_response.json()["id"]

    courier_id = None

    # TODO: передайте в тест данные, необходимые для авторизации.
    yield {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "id": courier_id,
    }

    # TODO: после завершения теста удалите созданного курьера.
    # DELETE /api/v1/courier/{id}
