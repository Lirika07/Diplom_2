import allure
from api_client import ApiClient
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
        response = ApiClient.login_user(payload)
        assert response.status_code == 200

    @allure.title("Ошибка при входе с неверным паролем")
    def test_login_wrong_password_unauthorized(self, create_user):
        user_data, _, _ = create_user
        payload = {
            "email": user_data["email"],
            "password": f"{user_data['password']}_wrong",
        }
        response = ApiClient.login_user(payload)
        assert response.status_code == 401

    @allure.title("Ошибка при входе с незарегистрированным email")
    def test_login_nonexistent_email_unauthorized(self):
        payload = {
            "email": f"{generate_random_string(10)}@yandex.ru",
            "password": generate_random_string(10),
        }
        response = ApiClient.login_user(payload)
        assert response.status_code == 401