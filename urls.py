class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"

    # Ручки пользователя
    REGISTER_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    USER_DATA = f"{BASE_URL}/api/auth/user"

    # Ручки заказов и ингредиентов
    ORDERS = f"{BASE_URL}/api/orders"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"