def test_place_order_success():
    """POST /store/order, place an order for an existing pet."""
    pass


def test_place_order_for_nonexistent_pet():
    """POST /store/order, should fail for non-existing pet."""
    pass


def test_get_order_by_id_success():
    """GET /store/order/{orderId}, retrieve order successfully."""
    pass


# @pytest.mark.parametrize()
def test_get_order_by_id_variations():
    """GET /store/order/{orderId}, check valid, missing, and invalid IDs."""
    pass


def test_delete_order_success():
    """DELETE /store/order/{orderId}, delete existing order."""
    pass


def test_delete_nonexistent_order():
    """DELETE /store/order/{orderId}, should return 404 for non-existent order."""
    pass
