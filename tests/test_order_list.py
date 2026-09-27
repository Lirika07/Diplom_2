import allure
import requests
from urls import Urls
from data import ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Получение заказов конкретного пользователя")
class TestOrderList:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authorized_user_success(self, create_user, get_ingredients):
        _, _, access_token = create_user
        headers = {"Authorization": access_token}

        # Создаем заказ для пользователя
        payload = {"ingredients": get_ingredients[:2]}
        requests.post(Urls.ORDERS, headers=headers, json=payload)

        # Запрашиваем историю заказов
        response = requests.get(Urls.ORDERS, headers=headers)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "orders" in response.json()
        assert len(response.json()["orders"]) >= 1

    @allure.title("Ошибка при попытке получить заказы неавторизованным пользователем")
    def test_get_orders_unauthorized_user_forbidden(self):
        response = requests.get(Urls.ORDERS)

        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == ErrorMessages.UNAUTHORIZED