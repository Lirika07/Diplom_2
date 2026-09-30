import pytest
from api_client import ApiClient
from data import generate_user_data


@pytest.fixture
def create_user():
    user_data = generate_user_data()
    response = ApiClient.create_user(user_data)
    access_token = response.json().get("accessToken")

    yield user_data, response, access_token

    if access_token:
        ApiClient.delete_user(access_token)


@pytest.fixture
def get_ingredients():
    response = ApiClient.get_ingredients()
    data = response.json().get("data", [])
    return [item["_id"] for item in data]