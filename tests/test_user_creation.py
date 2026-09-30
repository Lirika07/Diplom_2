import allure
import pytest
from api_client import ApiClient
from data import generate_user_data, ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self, create_user):
        _, response, _ = create_user
        assert response.status_code == 200

    @allure.title("Ошибка при создании уже зарегистрированного пользователя")
    def test_create_duplicate_user_forbidden(self, create_user):
        user_data, _, _ = create_user
        response = ApiClient.create_user(user_data)
        assert response.status_code == 403

    @allure.title("Ошибка при создании пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_forbidden(self, missing_field):
        user_data = generate_user_data()
        user_data.pop(missing_field)
        response = ApiClient.create_user(user_data)
        assert response.status_code == 403