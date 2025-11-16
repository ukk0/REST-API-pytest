import pytest

from resources.data_factories import build_pet


@pytest.mark.flaky(reruns=3)
@pytest.mark.integration
def test_full_pet_lifecycle(petstore_client, petstore_api_auth):
    """
    POST /pet - GET /pet/{id} - PUT /pet - DELETE /pet
    Validate creation, retrieval, update, and deletion of the same pet.
    """
    pet_payload = build_pet()
    create_response = petstore_client.create_pet(payload=pet_payload)
    pet_id = create_response.json()["id"]
    assert create_response.status_code == 200
    for key in pet_payload:
        assert pet_payload[key] == create_response.json()[key]

    get_response = petstore_client.get_pet_by_id(pet_id=pet_id)
    assert get_response.status_code == 200
    for key in pet_payload:
        assert pet_payload[key] == get_response.json()[key]

    update_payload = build_pet(
        pet_id=pet_id,
        name="Kissa",
        photo_url="pets.com/cat.png",
        status="pending",
    )
    update_response = petstore_client.update_pet(update_payload)
    assert update_response.status_code == 200
    for key in update_payload:
        assert update_payload[key] == update_response.json()[key]

    response = petstore_client.delete_pet_by_id(
        pet_id=pet_id, auth_header=petstore_api_auth
    )
    assert response.status_code == 200
