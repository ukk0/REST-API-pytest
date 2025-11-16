import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_update_user_success(petstore_client):
    """
    PUT /user/{username}, update existing user.
    """
    pass


@pytest.mark.regression
def test_update_user_with_invalid_name(petstore_client):
    """
    PUT /user/{username}, update invalid user.
    """
    pass
