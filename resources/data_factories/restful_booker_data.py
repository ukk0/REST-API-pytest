from typing import Any, Dict, Optional


def build_token_auth(
    username: str = "admin", password: str = "password123"
) -> Dict[str, Any]:
    return {"username": username, "password": password}


def build_api_key_header(key: str) -> Dict[str, Any]:
    return {"Authorization": f"Basic {key}"}


def build_token_header(cookie: str):
    return {"Cookie": f"token={cookie}"}


def build_query_params(**kwargs: Any) -> Dict[str, Any]:
    return dict(**kwargs)


def build_booking(
    fname: str = "Testy",
    lname: str = "McTester",
    price: float = 100.0,
    deposit: bool = True,
    check_in: str = "2026-01-01",
    check_out: str = "2026-01-10",
    additional_needs: Optional[str] = None,
    partial: bool = False,
    **overrides,
) -> Dict[str, Any]:
    """Builds booking payload for POST, PUT, or PATCH.
    - POST / PUT: return full payload
    - PATCH: set partial=True and pass only changed fields via overrides
    """
    payload = {
        "firstname": fname,
        "lastname": lname,
        "totalprice": price,
        "depositpaid": deposit,
        "bookingdates": {
            "checkin": check_in,
            "checkout": check_out,
        },
        "additionalneeds": additional_needs,
    }
    if partial:
        return dict(**overrides)
    return payload
