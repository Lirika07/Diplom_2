import pytest
import requests
from urls import Urls
from data import generate_user_data


@pytest.fixture
def create_user():
    user_data = generate_user_data()
    response = requests.post(Urls.REGISTER_USER, json=user_data)
    access_token = response.json().get("accessToken")

    yield user_data, response, access_token

    # Очистка данных после теста
    if access_token:
        requests.delete(Urls.USER_DATA, headers={"Authorization": access_token})


@pytest.fixture
def get_ingredients():
    response = requests.get(Urls.INGREDIENTS)
    data = response.json().get("data", [])
    ingredient_ids = [item["_id"] for item in data]
    return ingredient_ids