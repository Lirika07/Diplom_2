import allure
import requests
from urls import Urls


class ApiClient:

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(payload):
        return requests.post(Urls.REGISTER_USER, json=payload)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(payload):
        return requests.post(Urls.LOGIN_USER, json=payload)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token):
        return requests.delete(
            Urls.USER_DATA,
            headers={"Authorization": access_token},
        )

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        return requests.post(Urls.ORDERS, json=payload, headers=headers)

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_orders(access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        return requests.get(Urls.ORDERS, headers=headers)

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS)

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def update_user(payload, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        return requests.patch(Urls.USER_DATA, json=payload, headers=headers)