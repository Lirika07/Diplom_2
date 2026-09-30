import allure
from api_client import ApiClient
from data import ErrorMessages
from urls import Urls


@allure.epic("Stellar Burgers API")
@allure.feature("Получение заказов конкретного пользователя")
class TestOrderList:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authorized_user_success(self, create_user, get_ingredients):
        _, _, access_token = create_user
        payload = {"ingredients": get_ingredients[:2]}
        ApiClient.create_order(payload, access_token)

        response = ApiClient.get_orders(access_token)

        assert response.status_code == 200

    @allure.title("Ошибка при попытке получить заказы неавторизованным пользователем")
    def test_get_orders_unauthorized_user_forbidden(self):
        response = ApiClient.get_orders()

        assert response.status_code == 401