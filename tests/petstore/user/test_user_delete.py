import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user_success(petstore_client, valid_pet_id):
    """
    DELETE /user/{username}, delete user successfully.
    """
    pass


@pytest.mark.regression
def test_delete_nonexistent_user(petstore_client):
    """
    DELETE /user/{username}, should return 404.
    """
    pass
