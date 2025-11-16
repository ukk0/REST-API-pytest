from random import randint
from typing import Any, Dict


def build_pet(
    pet_id: str = randint(50, 100),
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


def build_petstore_auth_header(key: str) -> Dict[str, Any]:
    return {"api_key": f"{key}"}
