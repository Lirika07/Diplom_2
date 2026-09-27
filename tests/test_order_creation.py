import allure
import requests
from urls import Urls
from data import ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа авторизованным пользователем с ингредиентами")
    def test_create_order_authorized_with_ingredients_success(
        self, create_user, get_ingredients
    ):
        _, _, access_token = create_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": get_ingredients[:2]}

        response = requests.post(Urls.ORDERS, headers=headers, json=payload)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()

    @allure.title("Создание заказа неавторизованным пользователем с ингредиентами")
    def test_create_order_unauthorized_with_ingredients_success(self, get_ingredients):
        payload = {"ingredients": get_ingredients[:2]}

        response = requests.post(Urls.ORDERS, json=payload)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json()

    @allure.title("Ошибка при создании заказа без ингредиентов")
    def test_create_order_empty_ingredients_bad_request(self, create_user):
        _, _, access_token = create_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": []}

        response = requests.post(Urls.ORDERS, headers=headers, json=payload)

        assert response.status_code == 400
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.INGREDIENTS_MUST_BE_PROVIDED

    @allure.title("Ошибка при создании заказа с невалидным хешем ингредиента")
    def test_create_order_invalid_ingredient_hash_error(self, create_user):
        _, _, access_token = create_user
        headers = {"Authorization": access_token}
        payload = {"ingredients": ["invalid_hash_67890abcdef"]}

        response = requests.post(Urls.ORDERS, headers=headers, json=payload)

        # Сервер возвращает 500 при передаче невалидного ObjectId MongoDB
        assert response.status_code == 500