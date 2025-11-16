import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_login_logout_flow(petstore_client):
    """
    GET /user/login and /user/logout, valid login/logout sequence.
    NOTE: API does not include actual login functionality.
    """
    login_response = petstore_client.login_user(username="ukk0", password="not_real_password")
    assert login_response.status_code == 200

    logout_response = petstore_client.logout_user()
    assert logout_response.status_code == 200


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.skip(
    reason="Known API issue: Endpoint returns 200 without validating credentials."
)
@pytest.mark.parametrize("username, password", [
    (None, None),
    ("", "")
])
def test_login_user_invalid_credentials(petstore_client, username, password):
    """
    GET /user/login, test login with invalid types for credentials.
    """
    login_response = petstore_client.login_user(username=username, password=password)
    assert login_response.status_code == 401


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.skip(
    reason="Known API issue: Endpoint returns 200 without validating credentials."
)
def test_login_user_no_credentials(petstore_client):
    """
    GET /user/login, test login without adding credentials.
    """
    login_response = petstore_client.login_user(skip_auth=True)
    assert login_response.status_code == 401
