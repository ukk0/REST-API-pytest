import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_user_by_username(petstore_client, valid_user_id):
    """
    GET /user/{username}, with valid username.
    """
    response = petstore_client.get_user_by_name(username="ukk0")
    assert response.status_code == 200
    assert response.json()["username"] == "ukk0"


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, status_code, message",
    [
        ("user1", 404, "User not found"),
        ("", 405, None),
    ],
)
def test_get_user_by_username_variations(
    petstore_client, username, status_code, message
):
    """
    GET /user/{username}, with missing user or invalid username tests.
    """
    response = petstore_client.get_user_by_name(username=username)
    assert response.status_code == status_code
    if message:
        assert response.json()["message"] == message
