import allure
import pytest
import requests
from urls import Urls
from data import generate_user_data, ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self):
        user_data = generate_user_data()
        response = requests.post(Urls.REGISTER_USER, json=user_data)

        assert response.status_code == 200
        assert response.json().get("success") is True

        # Удаляем созданного пользователя
        access_token = response.json().get("accessToken")
        if access_token:
            requests.delete(Urls.USER_DATA, headers={"Authorization": access_token})

    @allure.title("Ошибка при создании уже зарегистрированного пользователя")
    def test_create_duplicate_user_forbidden(self, create_user):
        user_data, _, _ = create_user
        response = requests.post(Urls.REGISTER_USER, json=user_data)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.USER_ALREADY_EXISTS

    @allure.title("Ошибка при создании пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field_forbidden(self, missing_field):
        user_data = generate_user_data()
        user_data.pop(missing_field)

        response = requests.post(Urls.REGISTER_USER, json=user_data)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.REQUIRED_FIELDS_MISSING