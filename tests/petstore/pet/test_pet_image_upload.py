import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_successfully_upload_image(petstore_client, valid_pet_id):
    """
    POST pet/{pet_id}/uploadImage, add image for existing pet successfully.
    """
    response = petstore_client.upload_pet_image(
        pet_id=valid_pet_id, image_name="dog.png"
    )
    assert response.status_code == 200

    response_json = response.json()
    assert "type" in response_json
    assert "message" in response_json


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("pet_id", ["hundred", [10], None, 3.14])
def test_upload_image_with_invalid_pet_id(petstore_client, pet_id):
    """
    POST pet/{pet_id}/uploadImage, add image with invalid pet id should fail.
    """
    response = petstore_client.upload_pet_image(pet_id=pet_id, image_name="dog.png")
    assert response.status_code == 404


@pytest.mark.regression
@pytest.mark.skip(
    reason="Known API issue: Endpoint returns 200 without validating file format."
)
def test_upload_image_with_invalid_format(petstore_client, valid_pet_id):
    """
    POST pet/{pet_id}/uploadImage, add file with invalid format should fail.
    """
    response = petstore_client.upload_pet_image(
        pet_id=valid_pet_id, image_name="dog.txt"
    )
    assert response.status_code == 415


@pytest.mark.regression
def test_upload_image_with_invalid_header(petstore_client, valid_pet_id):
    """
    POST pet/{pet_id}/uploadImage, add image with invalid Content-Type header should fail.
    """
    response = petstore_client.upload_pet_image(
        pet_id=valid_pet_id,
        image_name="dog.png",
        headers=petstore_client._add_headers(),
    )
    assert response.status_code == 415
