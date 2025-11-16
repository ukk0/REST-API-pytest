import pytest

from resources.api_clients import PetStoreAPIClient, RestfulAPIClient
from resources.data_factories import (build_api_key_header, build_auth_payload,
                                      build_booking, build_token_header, build_pet, build_petstore_auth_header)

FAKE_RESTFUL_API_KEY = "YWRtaW46cGFzc3dvcmQxMjM="
FAKE_PETSTORE_API_KEY = "special-key"


@pytest.fixture(scope="session")
def restful_client():
    return RestfulAPIClient()


@pytest.fixture(scope="session")
def petstore_client():
    return PetStoreAPIClient()


@pytest.fixture(scope="session")
def auth_token(restful_client):
    return restful_client.fetch_auth_token(payload=build_auth_payload()).json()["token"]


@pytest.fixture(scope="session")
def api_key_auth():
    return build_api_key_header(key=FAKE_RESTFUL_API_KEY)


@pytest.fixture(scope="session")
def token_auth(auth_token):
    return build_token_header(cookie=auth_token)


@pytest.fixture(scope="function")
def valid_booking_id(restful_client):
    return restful_client.create_booking(payload=build_booking()).json()["bookingid"]


@pytest.fixture(scope="function")
def valid_pet_id(petstore_client):
    return petstore_client.create_pet(payload=build_pet()).json()["id"]


@pytest.fixture(scope="session")
def petstore_api_auth(petstore_client):
    return build_petstore_auth_header(key=FAKE_PETSTORE_API_KEY)
