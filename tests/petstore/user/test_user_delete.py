import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user_success(petstore_client, valid_user_id):
    """
    DELETE /user/{username}, delete user successfully.
    """
    response = petstore_client.delete_user(username="ukk0")
    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.parametrize("username", ["UserDoesNotExist1-9", 3.14159, None, {"name": "ukk0"}])
def test_delete_nonexistent_user(petstore_client, username):
    """
    DELETE /user/{username}, nonexistent & invalid usernames should return 404.
    """
    response = petstore_client.delete_user(username=username)
    assert response.status_code == 404
