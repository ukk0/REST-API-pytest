from typing import Any, Dict, Optional

from requests import Response

from resources.api_clients.base_api_client import BaseClient


class PetStoreAPIClient(BaseClient):
    def __init__(self):
        base_url = "https://petstore.swagger.io/v2/"
        super().__init__(base_url)

    def create_entity(self, entity: str, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url=entity, headers=self._add_headers(), method="POST", json=payload
        )

    def update_pet(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="pet", headers=self._add_headers(), method="PUT", json=payload
        )

    def get_pet_by_id(self, pet_id: str) -> Response:
        return self._api_request(
            url=f"pet/{pet_id}", headers=self._add_headers(), method="GET"
        )

    def get_pet_by_status(self, query_params: Optional[Dict[str, str]] = None) -> Response:
        return self._api_request(
            url=self._add_params_to_url(url="pet/findPetsByStatus", params=query_params),
            headers=self._add_headers(),
            method="GET",
        )

    def delete_pet_by_id(self, pet_id: str, auth_header: Dict[str, str]) -> Response:
        return self._api_request(
            url=f"pet/{pet_id}",
            headers=self._add_headers(auth_header=auth_header),
            method="DELETE",
        )

    def get_store_inventory(self) -> Response:
        return self._api_request(
            url="store/inventory", headers=self._add_headers(), method="GET",
        )

    def get_order_by_id(self, order_id: str) -> Response:
        return self._api_request(
            url=f"store/order/{order_id}", headers=self._add_headers(), method="GET"
        )

    def delete_order_by_id(self, order_id: str) -> Response:
        return self._api_request(
            url=f"store/order/{order_id}", headers=self._add_headers(), method="DELETE"
        )

