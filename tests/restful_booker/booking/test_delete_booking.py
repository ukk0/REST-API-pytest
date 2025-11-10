import pytest

from resources.data_factories import build_api_key_header, build_token_header


@pytest.mark.parametrize(
    "auth_method", ["api_key", "token_auth"], ids=["valid_api_key", "valid_token"]
)
def test_delete_booking_valid(
    restful_client, auth_method, valid_booking_id, api_key_auth, token_auth
):
    """
    DELETE /booking/{id}, valid deletion with valid auth method.
    """
    if auth_method == "api_key":
        response = restful_client.delete_booking_by_id(
            booking_id=valid_booking_id, auth_header=api_key_auth
        )
        assert response.status_code == 201

    elif auth_method == "token_auth":
        response = restful_client.delete_booking_by_id(
            booking_id=valid_booking_id, auth_header=token_auth
        )
        assert response.status_code == 201


def test_delete_booking_invalid(restful_client, api_key_auth, valid_booking_id):
    """
    DELETE /booking/{id}, test deletion for non-existing / already deleted id.
    """
    restful_client.delete_booking_by_id(
        booking_id=valid_booking_id, auth_header=api_key_auth
    )
    assert (
        restful_client.delete_booking_by_id(
            booking_id=valid_booking_id, auth_header=api_key_auth
        ).status_code
        == 405
    )


@pytest.mark.parametrize(
    "auth_method",
    ["api_key", "token_auth", "no_auth"],
    ids=["invalid_api_key", "invalid_token", "no_auth_method"],
)
def test_delete_booking_without_valid_auth_should_fail(
    restful_client, auth_method, valid_booking_id
):
    """
    DELETE /booking/{id}, without valid auth should fail
    """
    if auth_method == "api_key":
        response = restful_client.delete_booking_by_id(
            booking_id=valid_booking_id, auth_header=build_api_key_header(key="invalid")
        )
        assert response.status_code == 403

    elif auth_method == "token_auth":
        response = restful_client.delete_booking_by_id(
            booking_id=valid_booking_id,
            auth_header=build_token_header(cookie="invalid"),
        )
        assert response.status_code == 403

    elif auth_method == "no_auth":
        response = restful_client.delete_booking_by_id(
            booking_id=valid_booking_id, auth_header={}
        )
        assert response.status_code == 403
