import pytest

from resources.data_factories import (build_api_key_header, build_booking,
                                      build_token_header)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "auth_method", ["api_key", "token_auth"], ids=["valid_api_key", "valid_token"]
)
def test_update_booking_put_valid(
    restful_client, valid_booking_id, api_key_auth, token_auth, auth_method
):
    """
    PUT /booking/{id}, valid full payload update with valid auth methods.
    """
    update_payload = build_booking(
        fname="Julius", lname="Caesar", price=10.0, deposit=False
    )

    if auth_method == "api_key":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=api_key_auth,
            payload=update_payload,
        )
        assert response.status_code == 200

    elif auth_method == "token_auth":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=token_auth,
            payload=update_payload,
        )
        assert response.status_code == 200

    assert update_payload == response.json()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "auth_method", ["api_key", "token_auth"], ids=["valid_api_key", "valid_token"]
)
def test_update_booking_patch_valid(
    restful_client, valid_booking_id, api_key_auth, token_auth, auth_method
):
    """
    PATCH /booking/{id}, valid partial update with valid auth methods.
    """
    update_payload = build_booking(partial=True, totalprice=20.0)

    if auth_method == "api_key":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=api_key_auth,
            payload=update_payload,
            partial_update=True,
        )
        assert response.status_code == 200

    elif auth_method == "token_auth":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=token_auth,
            payload=update_payload,
            partial_update=True,
        )
        assert response.status_code == 200

    assert update_payload["totalprice"] == response.json()["totalprice"]


@pytest.mark.regression
@pytest.mark.skip(
    reason="Known API issue: Endpoint returns 200 and ignores unsupported values."
)
@pytest.mark.parametrize(
    "update_payload",
    [
        {"totalprice": None},
        {"new_field": 100},
        {"depositpaid": "Yes"},
    ], ids=["invalid_price", "unsupported_field", "invalid_deposit"]
)
def test_partial_update_with_invalid_value(
    restful_client, valid_booking_id, api_key_auth, update_payload
):
    """
    PATCH /booking/{id}, partial update with invalid values for update.
    """
    response = restful_client.update_booking_by_id(
        booking_id=valid_booking_id,
        auth_header=api_key_auth,
        payload=update_payload,
        partial_update=True,
    )
    assert response.status_code == 400


@pytest.mark.regression
def test_update_booking_with_invalid_payload(
    restful_client, valid_booking_id, api_key_auth
):
    """
    PUT /booking/{id}, full update with invalid payload should fail.
    """
    payload = build_booking()
    del payload["firstname"]

    response = restful_client.update_booking_by_id(
        booking_id=valid_booking_id, auth_header=api_key_auth, payload=payload
    )
    assert response.status_code == 400


@pytest.mark.regression
@pytest.mark.parametrize(
    "auth_method, partial",
    [
        ("api_key", False),
        ("token_auth", False),
        ("no_auth", False),
        ("api_key", True),
        ("token_auth", True),
        ("no_auth", True),
    ],
    ids=[
        "put_invalid_api_key",
        "put_invalid_token",
        "put_no_auth_method",
        "patch_invalid_api_key",
        "patch_invalid_token",
        "patch_no_auth_method",
    ],
)
def test_update_booking_without_valid_auth_should_fail(
    restful_client, valid_booking_id, auth_method, partial
):
    """
    PUT/PATCH /booking/{id}, without valid auth method should fail
    """
    payload = build_booking()

    if auth_method == "api_key":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=build_api_key_header(key="invalid"),
            payload=payload,
            partial_update=partial,
        )
        assert response.status_code == 403

    elif auth_method == "token_auth":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=build_token_header(cookie="invalid"),
            payload=payload,
            partial_update=partial,
        )
        assert response.status_code == 403

    elif auth_method == "no_auth":
        response = restful_client.update_booking_by_id(
            booking_id=valid_booking_id,
            auth_header={},
            payload=payload,
            partial_update=partial,
        )
        assert response.status_code == 403
