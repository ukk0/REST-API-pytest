from pathlib import Path
from typing import Any, Dict, List, Optional

from requests import Response

from resources.api_clients.base_api_client import BaseClient
from resources.data_factories import build_query_params


class PetStoreAPIClient(BaseClient):
    def __init__(self):
        base_url = "https://petstore.swagger.io/v2"
        super().__init__(base_url)

    def create_pet(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="pet", headers=self._add_headers(), method="POST", json=payload
        )

    def upload_pet_image(
        self,
        pet_id: int,
        image_name: str,
        headers: Dict[str, str] = None,
    ) -> Response:
        # We need to specifically construct the path for when we call this from /tests
        base = Path(__file__).resolve().parents[1]
        file_path = base / "test_data" / image_name

        with open(file_path, "rb") as f:
            files = {"file": (image_name, f, "image/png")}
            return self._api_request(
                url=f"pet/{pet_id}/uploadImage",
                method="POST",
                headers=headers if headers else {"User-Agent": "Automatic-API-test"},
                files=files,
            )

    def update_pet(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="pet", headers=self._add_headers(), method="PUT", json=payload
        )

    def get_pet_by_id(self, pet_id: str) -> Response:
        return self._api_request(
            url=f"pet/{pet_id}", headers=self._add_headers(), method="GET"
        )

    def get_pet_by_status(
        self, query_params: Optional[Dict[str, str]] = None
    ) -> Response:
        return self._api_request(
            url=self._add_params_to_url(url="pet/findByStatus", params=query_params),
            headers=self._add_headers(),
            method="GET",
        )

    def delete_pet_by_id(
        self, pet_id: str, auth_header: Optional[Dict[str, str]] = None
    ) -> Response:
        return self._api_request(
            url=f"pet/{pet_id}",
            headers=self._add_headers(auth_header=auth_header),
            method="DELETE",
        )

    def get_store_inventory(self) -> Response:
        return self._api_request(
            url="store/inventory",
            headers=self._add_headers(),
            method="GET",
        )

    def create_store_order(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="store/order", headers=self._add_headers(), method="POST", json=payload
        )

    def get_order_by_id(self, order_id: str) -> Response:
        return self._api_request(
            url=f"store/order/{order_id}", headers=self._add_headers(), method="GET"
        )

    def delete_order_by_id(self, order_id: str) -> Response:
        return self._api_request(
            url=f"store/order/{order_id}", headers=self._add_headers(), method="DELETE"
        )

    def create_user(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="user", headers=self._add_headers(), method="POST", json=payload
        )

    def create_list_of_users(self, payload: List[Dict[str, Any]]) -> Response:
        return self._api_request(
            url="user/createWithList",
            headers=self._add_headers(),
            method="POST",
            json=payload,
        )

    def update_user(self, username: str, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url=f"user/{username}",
            headers=self._add_headers(),
            method="PUT",
            json=payload,
        )

    def delete_user(self, username: str) -> Response:
        return self._api_request(
            url=f"user/{username}",
            headers=self._add_headers(),
            method="DELETE",
        )

    def get_user_by_name(self, username: str) -> Response:
        return self._api_request(
            url=f"user/{username}",
            headers=self._add_headers(),
            method="GET",
        )

    def login_user(
        self, username: str = None, password: str = None, skip_auth: bool = False
    ) -> Response:
        query_params = build_query_params(username=username, password=password)
        if not skip_auth:
            url = self._add_params_to_url(url="user/login", params=query_params)
        else:
            url = "user/login"
        return self._api_request(
            url=url,
            headers=self._add_headers(),
            method="GET",
        )

    def logout_user(self):
        return self._api_request(
            url="user/logout",
            headers=self._add_headers(),
            method="GET",
        )
