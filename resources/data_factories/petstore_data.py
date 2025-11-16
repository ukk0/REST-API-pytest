from random import randint
from typing import Any, Dict


def build_petstore_auth_header(key: str) -> Dict[str, Any]:
    return {"api_key": f"{key}"}


def build_pet(
    pet_id: int = randint(500, 1000),
    name: str = "Koira",
    photo_url: str = "pets.com/dog.png",
    status: str = "available",
) -> Dict[str, Any]:
    return {
        "id": pet_id,
        "name": name,
        "photoUrls": [photo_url],
        "status": status,
    }


def build_order(
    order_id: int = randint(500, 1000),
    pet_id: int = 0,
    quantity: int = 1,
    shipdate: str = "2025-11-16",
    status: str = "placed",
    complete: bool = False,
) -> Dict[str, Any]:
    return {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": f"{shipdate}T00:00:00.000+0000",
        "status": status,
        "complete": complete,
    }


def build_user(
    user_id: int = randint(500, 1000),
    username: str = "ukk0",
    fname: str = "Testy",
    lname: str = "McTester",
    email: str = "email@test.com",
    password: str = "very_secret",
    phone: str = "12345678",
    user_status: int = 0,
) -> Dict[str, Any]:
    return {
        "id": user_id,
        "username": username,
        "firstName": fname,
        "lastName": lname,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status,
    }
