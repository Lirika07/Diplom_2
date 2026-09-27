import allure
import pytest
import requests
from urls import Urls
from data import generate_random_string, ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Изменение данных пользователя")
class TestUserUpdate:

    @allure.title("Успешное изменение имени и email с авторизацией")
    @pytest.mark.parametrize(
        "field_to_update, new_value",
        [
            ("name", f"Updated_{generate_random_string(5)}"),
            ("email", f"{generate_random_string(8)}@yandex.ru"),
        ],
    )
    def test_update_user_field_with_auth_success(
        self, create_user, field_to_update, new_value
    ):
        _, _, access_token = create_user
        headers = {"Authorization": access_token}
        payload = {field_to_update: new_value}

        response = requests.patch(Urls.USER_DATA, headers=headers, json=payload)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json()["user"][field_to_update] == new_value

    @allure.title("Ошибка при изменении данных без авторизации")
    def test_update_user_without_auth_unauthorized(self, create_user):
        payload = {"name": f"Anonymous_{generate_random_string(5)}"}

        response = requests.patch(Urls.USER_DATA, json=payload)

        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.UNAUTHORIZED