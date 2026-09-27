import allure
import requests
from urls import Urls
from data import generate_random_string, ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Авторизация пользователя")
class TestUserLogin:

    @allure.title("Успешный вход под существующим пользователем")
    def test_login_existing_user_success(self, create_user):
        user_data, _, _ = create_user
        payload = {
            "email": user_data["email"],
            "password": user_data["password"],
        }

        response = requests.post(Urls.LOGIN_USER, json=payload)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Ошибка при входе с неверным паролем")
    def test_login_wrong_password_unauthorized(self, create_user):
        user_data, _, _ = create_user
        payload = {
            "email": user_data["email"],
            "password": f"{user_data['password']}_wrong",
        }

        response = requests.post(Urls.LOGIN_USER, json=payload)

        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.INCORRECT_CREDENTIALS

    @allure.title("Ошибка при входе с незарегистрированным email")
    def test_login_nonexistent_email_unauthorized(self):
        payload = {
            "email": f"{generate_random_string(10)}@yandex.ru",
            "password": generate_random_string(10),
        }

        response = requests.post(Urls.LOGIN_USER, json=payload)

        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.INCORRECT_CREDENTIALS