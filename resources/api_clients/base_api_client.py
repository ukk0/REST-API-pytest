from typing import Any, Dict, Optional

from requests import Response, request


class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _api_request(
        self,
        url: str,
        headers: Dict[str, str],
        method: str = "GET",
        timeout: int = 100,
        json: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Response:
        url = f"{self.base_url}/{url}"
        return request(
            method=method,
            url=url,
            timeout=timeout,
            headers=headers,
            json=json,
            **kwargs,
        )

    @staticmethod
    def _add_headers(auth_header: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Automatic-API-test",
        }
        if auth_header:
            headers.update(auth_header)
        return headers

    @staticmethod
    def _add_params_to_url(url: str, params: Dict[str, Any]) -> str:
        if not params:
            return url

        query_params = [f"{x}={y}" for x, y in params.items()]
        url += "?" + "&".join(query_params)
        return url
