import pytest

from resources.data_factories import build_order


@pytest.mark.smoke
@pytest.mark.regression
def test_place_order_success(petstore_client, valid_pet_id):
    """
    POST /store/order, place an order for an existing pet.
    """
    order_payload = build_order(pet_id=valid_pet_id)
    response = petstore_client.create_store_order(payload=order_payload)
    assert response.status_code == 200

    response_json = response.json()
    for k, v in order_payload.items():
        assert response_json[k] == v


@pytest.mark.regression
@pytest.mark.skip(
    reason="Known API issue: Endpoint does not validate whether pet exists. If not, it will create one"
)
def test_place_order_for_nonexistent_pet(petstore_client):
    """
    POST /store/order, should fail for non-existing pet.
    """
    order_payload = build_order(pet_id=-123456789)

    response = petstore_client.create_store_order(order_payload)
    assert response.status_code == 404


@pytest.mark.smoke
@pytest.mark.regression
def test_get_order_by_id_success(petstore_client):
    """
    GET /store/order/{orderId}, retrieve order details successfully.
    """
    order_payload = build_order(order_id=1)

    response = petstore_client.create_store_order(order_payload)
    assert response.status_code == 200

    response_json = response.json()
    for k, v in order_payload.items():
        assert response_json[k] == v


@pytest.mark.regression
@pytest.mark.parametrize(
    "order_id, status_code",
    [(1, 200), ("2", 200), (9, 404), (None, 404), ("ten", 404), ("", 405), (-1, 404)],
)
def test_get_order_by_id_variations(petstore_client, order_id, status_code):
    """
    GET /store/order/{orderId}, check valid, missing and invalid IDs.
    """
    response = petstore_client.get_order_by_id(order_id=order_id)
    assert response.status_code == status_code


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_order_success(petstore_client, valid_order_id):
    """
    DELETE /store/order/{orderId}, delete existing order.
    """
    response = petstore_client.delete_order_by_id(order_id=valid_order_id)
    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.parametrize(
    "order_id, status_code",
    [(1, 200), ("2", 200), (9, 404), (None, 404), ("ten", 404), ("", 405), (-1, 404)],
)
def test_delete_order_by_id_variations(petstore_client, order_id, status_code):
    """
    DELETE /store/order/{orderId}, check valid, missing and invalid IDs.
    """
    response = petstore_client.delete_order_by_id(order_id=order_id)
    assert response.status_code == status_code
