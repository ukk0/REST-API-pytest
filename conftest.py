import pytest

from resources.api_clients import RestfulAPIClient, PetStoreAPIClient
from resources.data_factories import (build_api_key_header, build_auth_payload,
                                      build_token_header)

FAKE_API_KEY = "YWRtaW46cGFzc3dvcmQxMjM=]"


@pytest.fixture(scope="session")
def restful_client():
    return RestfulAPIClient()


@pytest.fixture(scope="session")
def petstore_client():
    return PetStoreAPIClient()


@pytest.fixture(scope="session")
def auth_token(restful_client):
    return restful_client.fetch_auth_token(build_auth_payload()).json()["token"]


@pytest.fixture(scope="session")
def api_key_auth():
    return build_api_key_header(key=FAKE_API_KEY)


@pytest.fixture(scope="session")
def token_auth(auth_token):
    return build_token_header(cookie=auth_token)
