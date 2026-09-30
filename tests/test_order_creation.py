import allure
from api_client import ApiClient
from data import ErrorMessages


@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа авторизованным пользователем с ингредиентами")
    def test_create_order_authorized_with_ingredients_success(
        self, create_user, get_ingredients
    ):
        _, _, access_token = create_user
        payload = {"ingredients": get_ingredients[:2]}
        response = ApiClient.create_order(payload, access_token)
        assert response.status_code == 200

    @allure.title("Создание заказа неавторизованным пользователем с ингредиентами")
    def test_create_order_unauthorized_with_ingredients_success(self, get_ingredients):
        payload = {"ingredients": get_ingredients[:2]}
        response = ApiClient.create_order(payload)
        assert response.status_code == 200

    @allure.title("Ошибка при создании заказа без ингредиентов")
    def test_create_order_empty_ingredients_bad_request(self, create_user):
        _, _, access_token = create_user
        payload = {"ingredients": []}
        response = ApiClient.create_order(payload, access_token)
        assert response.status_code == 400

    @allure.title("Ошибка при создании заказа с невалидным хешем ингредиента")
    def test_create_order_invalid_ingredient_hash_error(self, create_user):
        _, _, access_token = create_user
        payload = {"ingredients": ["invalid_hash_67890abcdef"]}
        response = ApiClient.create_order(payload, access_token)
        assert response.status_code == 500