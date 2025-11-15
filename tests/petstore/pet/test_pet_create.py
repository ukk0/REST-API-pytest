import pytest

from resources.data_factories import build_pet


@pytest.mark.smoke
@pytest.mark.regression
def test_add_new_pet_success(petstore_client):
    """
    POST /pet, create new pet successfully.
    """
    pet_payload = build_pet()
    response = petstore_client.create_pet(payload=pet_payload)
    assert response.status_code == 200

    json_response = response.json()
    for key in pet_payload:
        assert pet_payload[key] == json_response[key]


@pytest.mark.regression
def test_add_pet_with_missing_payload(petstore_client):
    """
    POST /pet, should fail when no payload is provided.
    """
    response = petstore_client.create_pet(payload=None)
    assert response.status_code == 405


@pytest.mark.regression
@pytest.mark.parametrize("field, wrong_value", [
    ("id", "ten"),
    ("name", {}),
    ("photoUrls", "not_a_list"),
    ("status", []),
])
def test_add_pet_with_invalid_data_types(petstore_client, field, wrong_value):
    """
    POST /pet, should fail when invalid data type is provided.
    """
    pet_payload = build_pet()
    pet_payload[field] = wrong_value

    response = petstore_client.create_pet(payload=pet_payload)
    assert response.status_code == 500


@pytest.mark.skip(
    reason="Known API issue: Endpoint returns 200 despite required field missing."
)
@pytest.mark.parametrize("req_field", ["name", "photoUrls"])
def test_add_pet_with_missing_required_fields(petstore_client, req_field):
    """
    POST /pet, should fail when a required field is missing.
    """
    pet_payload = build_pet()
    del pet_payload[req_field]

    response = petstore_client.create_pet(payload=pet_payload)
    assert response.status_code == 405
