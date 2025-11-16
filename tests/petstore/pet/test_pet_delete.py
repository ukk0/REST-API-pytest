import pytest

from resources.data_factories import build_petstore_auth_header


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_pet_success(petstore_client, valid_pet_id, petstore_api_auth):
    """
    DELETE /pet/{petId}, delete an existing pet successfully with valid id and auth.
    """
    response = petstore_client.delete_pet_by_id(
        pet_id=valid_pet_id, auth_header=petstore_api_auth
    )
    assert response.status_code == 200


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("pet_id", [-1, 3.14159, "hundred", None])
def test_delete_pet_with_invalid_id(petstore_client, petstore_api_auth, pet_id):
    """
    DELETE /pet/{petId}, trying to delete pet with invalid/non-existent id value fails.
    """
    response = petstore_client.delete_pet_by_id(
        pet_id=pet_id, auth_header=petstore_api_auth
    )
    assert response.status_code == 404


@pytest.mark.regression
@pytest.mark.flaky(reruns=3)
@pytest.mark.parametrize(
    "api_key, status_code",
    [
        ("", 404),
        ("wrong-key", 404),
        (None, 404),
    ],
)
def test_delete_pet_without_auth(petstore_client, valid_pet_id, api_key, status_code):
    """
    DELETE /pet/{petId}, deleting existing pet with missing api key or missing
    auth header should fail.
    NOTE: The API is flaky when it comes to auth req => it will occasionally throw 200 here.
    Using the pytest-rerunfails just to showcase the usage of the plugin here.
    """
    if api_key is not None:
        header = build_petstore_auth_header(key=api_key)
        response = petstore_client.delete_pet_by_id(
            pet_id=valid_pet_id, auth_header=header
        )
    else:
        response = petstore_client.delete_pet_by_id(pet_id=valid_pet_id)
    assert response.status_code == status_code
