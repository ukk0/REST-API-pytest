import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_get_inventory_returns_valid_counts(petstore_client):
    """
    GET /store/inventory, should return dict of statuses with counts.
    """
    response = petstore_client.get_store_inventory()
    assert response.status_code == 200

    response_json = response.json()
    assert isinstance(response_json["available"], int)
    assert isinstance(response_json["pending"], int)
    assert isinstance(response_json["sold"], int)
