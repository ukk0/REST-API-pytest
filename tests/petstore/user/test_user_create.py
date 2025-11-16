from random import randint

import pytest

from resources.data_factories import build_user


@pytest.mark.smoke
@pytest.mark.regression
def test_create_user_success(petstore_client):
    """
    POST /user, create a user successfully.
    """
    user_payload = build_user()
    response = petstore_client.create_user(payload=user_payload)
    assert response.status_code == 200
    assert user_payload["id"] == int(response.json()["message"])


@pytest.mark.smoke
@pytest.mark.regression
def test_create_users_with_list(petstore_client):
    """
    POST /user/createWithList, create multiple users with different ids.
    """
    first_user_payload = build_user(randint(500, 1000))
    second_user_payload = build_user(randint(500, 1000))
    response = petstore_client.create_list_of_users(
        payload=[first_user_payload, second_user_payload]
    )
    assert response.status_code == 200


@pytest.mark.regression
def test_create_user_with_missing_payload(petstore_client):
    """
    POST /user, should fail when no payload is provided.
    """
    response = petstore_client.create_user(payload=None)
    assert response.status_code == 405


@pytest.mark.regression
@pytest.mark.parametrize(
    "field, wrong_value",
    [
        ("id", "ten"),
        ("username", {"name": "ukk0"}),
        ("userStatus", False),
        ("phone", []),
    ],
)
def test_create_user_with_invalid_data_types(petstore_client, field, wrong_value):
    """
    POST /user, should fail when invalid data type is provided.
    """
    user_payload = build_user()
    user_payload[field] = wrong_value

    response = petstore_client.create_user(payload=user_payload)
    assert response.status_code == 500
