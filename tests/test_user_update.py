import allure
import pytest
from api_client import ApiClient
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
        payload = {field_to_update: new_value}

        response = ApiClient.update_user(payload, access_token)

        assert response.status_code == 200

    @allure.title("Ошибка при изменении данных без авторизации")
    def test_update_user_without_auth_unauthorized(self, create_user):
        payload = {"name": f"Anonymous_{generate_random_string(5)}"}

        response = ApiClient.update_user(payload)

        assert response.status_code == 401