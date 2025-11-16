import pytest

from resources.data_factories import build_query_params


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(petstore_client, status):
    """
    GET /pet/findByStatus, validate various status filters.
    """
    query_params = build_query_params(status=status)
    response = petstore_client.get_pet_by_status(query_params=query_params)
    assert response.status_code == 200

    for pet in response.json():
        assert pet["status"] == status


@pytest.mark.smoke
@pytest.mark.regression
def test_get_pet_by_id(petstore_client, valid_pet_id):
    """
    GET /pet/{petId}, successful response for existing pet.
    """
    response = petstore_client.get_pet_by_id(pet_id=valid_pet_id)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json["id"] == valid_pet_id
    assert response_json["name"] == "Koira"
    assert response_json["photoUrls"][0] == "pets.com/dog.png"
    assert response_json["status"] == "available"


@pytest.mark.regression
@pytest.mark.parametrize(
    "pet_id, status_code",
    [
        (100000000000, 404),
        (3.14159, 404),
        ("hundred", 404),
        (None, 404),
        ("", 405),
    ],
    ids=["not_found_id", "float_id", "string_id", "none_id", "empty_string_id"],
)
def test_get_pet_by_bad_id(petstore_client, pet_id, status_code):
    """
    GET /pet/{petId}, check responses missing, and bad IDs.
    NOTE: The API does quite bad job of validating ID, responding
    with 404s to bad format instead of 400.
    """
    response = petstore_client.get_pet_by_id(pet_id=pet_id)
    assert response.status_code == status_code
