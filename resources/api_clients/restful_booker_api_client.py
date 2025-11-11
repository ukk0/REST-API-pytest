from typing import Any, Dict, Optional

from requests import Response

from resources.api_clients.base_api_client import BaseClient


class RestfulAPIClient(BaseClient):
    def __init__(self):
        base_url = "https://restful-booker.herokuapp.com/"
        super().__init__(base_url)

    def fetch_auth_token(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="auth",
            headers=self._add_headers(),
            method="POST",
            json=payload,
        )

    def ping_api(self) -> Response:
        return self._api_request(url="ping", headers=self._add_headers(), method="GET")

    def create_booking(self, payload: Dict[str, Any]) -> Response:
        return self._api_request(
            url="booking", headers=self._add_headers(), method="POST", json=payload
        )

    def get_all_booking_ids(
        self, query_params: Optional[Dict[str, Any]] = None
    ) -> Response:
        return self._api_request(
            url=self._add_params_to_url(url="booking", params=query_params),
            headers=self._add_headers(),
            method="GET",
        )

    def get_booking_by_id(self, booking_id: str) -> Response:
        return self._api_request(
            url=f"booking/{booking_id}", headers=self._add_headers(), method="GET"
        )

    def update_booking_by_id(
        self,
        booking_id: str,
        auth_header: Dict[str, str],
        payload: Dict[str, Any],
        partial_update: bool = False,
    ) -> Response:
        return self._api_request(
            url=f"booking/{booking_id}",
            headers=self._add_headers(auth_header=auth_header),
            method="PATCH" if partial_update else "PUT",
            json=payload,
        )

    def delete_booking_by_id(
        self, booking_id: str, auth_header: Dict[str, str]
    ) -> Response:
        return self._api_request(
            url=f"booking/{booking_id}",
            headers=self._add_headers(auth_header=auth_header),
            method="DELETE",
        )
