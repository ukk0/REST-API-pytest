import pytest

from resources.data_factories import build_pet


@pytest.mark.smoke
@pytest.mark.regression
def test_update_existing_pet_put_success(petstore_client, valid_pet_id):
    """
    PUT /pet, update existing pet fully.
    """
    update_payload = build_pet(
        pet_id=valid_pet_id, name="Kissa", photo_url="pets.com/cat.png", status="pending"
    )
    update_response = petstore_client.update_pet(update_payload)
    assert update_response.status_code == 200

    response_json = update_response.json()
    for k, v in update_payload.items():
        assert response_json[k] == v


@pytest.mark.regression
def test_update_pet_with_missing_payload(petstore_client):
    """
    PUT /pet, should fail when no payload is provided.
    """
    response = petstore_client.update_pet(payload=None)
    assert response.status_code == 405


@pytest.mark.regression
@pytest.mark.skip(
    reason="Known API issue: Endpoint returns 200 without correctly validating ID."
)
@pytest.mark.parametrize(
    "pet_id, status_code", [
        (9999999999999, 404),
        (None, 400),
    ], ids=["nonexistent_pet_id", "invalid_pet_id"]
)
def test_update_pet_with_invalid_id(petstore_client, pet_id, status_code):
    """
    PUT /pet, should return 400 for invalid id in payload.
    """
    update_payload = build_pet(
        pet_id=pet_id, name="Kissa", photo_url="pets.com/cat.png", status="pending"
    )
    update_response = petstore_client.update_pet(update_payload)
    assert update_response.status_code == status_code
