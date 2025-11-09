import pytest

from resources.data_factories import build_auth_payload


def test_generate_token_valid_credentials(restful_client):
    """POST /auth => valid username/password should return 200 status and a token."""
    response = restful_client.fetch_auth_token(payload=build_auth_payload())
    assert response.status_code == 200
    assert response.json()["token"]


@pytest.mark.parametrize(
    "username, password, status_code",
    [
        ("admin", "wrong_password", 200),
        ("wrong_user", "wrong_password", 200),
        ("username", None, 200),
        (None, "wrong_password", 200),
    ],
)
def test_generate_token_wrong_or_missing_credentials(
    restful_client, username, password, status_code
):
    """POST /auth => wrong/missing username/password should fail.
    NOTE: The endpoint incorrectly returns status code 200 for bad request."""
    response = restful_client.fetch_auth_token(
        payload=build_auth_payload(username=username, password=password)
    )
    assert response.status_code == status_code
    assert response.json()["reason"] == "Bad credentials"
