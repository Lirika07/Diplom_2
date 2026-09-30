import random
import string


def generate_random_string(length=8):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_user_data():
    email = f"{generate_random_string(8)}@yandex.ru"
    password = generate_random_string(10)
    name = f"User_{generate_random_string(5)}"
    return {
        "email": email,
        "password": password,
        "name": name,
    }


class ErrorMessages:
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS_MISSING = "Email, password and name are required fields"
    INCORRECT_CREDENTIALS = "email or password are incorrect"
    UNAUTHORIZED = "You should be authorised"
    INGREDIENTS_MUST_BE_PROVIDED = "Ingredient ids must be provided"