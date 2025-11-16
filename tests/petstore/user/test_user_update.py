import pytest

from resources.data_factories import build_user


@pytest.mark.smoke
@pytest.mark.regression
def test_update_user_success(petstore_client, valid_username):
    """
    PUT /user/{username}, update existing user.
    """
    update_payload = build_user(fname="Alan", lname="Shepard", username="Commander")
    response = petstore_client.update_user(username="Keijo", payload=update_payload)
    assert response.status_code == 200
    assert int(response.json()["message"]) == update_payload["id"]


@pytest.mark.regression
def test_update_user_with_missing_payload(petstore_client, valid_user_id):
    """
    PUT /user, should fail when no payload is provided.
    """
    response = petstore_client.update_user(username="ukk0", payload=None)
    assert response.status_code == 405


@pytest.mark.regression
def test_update_user_with_empty_name(petstore_client):
    """
    PUT /user/{username}, update empty username.
    """
    response = petstore_client.update_user(username="", payload=build_user())
    assert response.status_code == 405
