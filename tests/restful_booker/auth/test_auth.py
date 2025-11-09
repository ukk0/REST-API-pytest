import pytest


def test_generate_token_valid_credentials():
    """POST /auth, valid username/password should return token."""
    pass


@pytest.mark.parametrize()
def test_generate_token_missing_credential():
    """POST /auth, missing username/password should fail with 400."""
    pass
