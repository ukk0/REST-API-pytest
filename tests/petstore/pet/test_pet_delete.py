import pytest


def test_delete_pet_success():
    """DELETE /pet/{petId}, delete an existing pet."""
    pass


def test_delete_nonexistent_pet():
    """DELETE /pet/{petId}, deleting non-existent pet returns 404."""
    pass


def test_delete_pet_without_auth():
    """DELETE /pet/{petId}, delete an existing pet, but missing required auth."""
    pass
