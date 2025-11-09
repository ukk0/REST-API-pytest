def test_ping_response(restful_client):
    """GET /ping => should return 201 status."""
    response = restful_client.ping_api()
    assert response.status_code == 201
