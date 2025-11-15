import pytest

from resources.data_factories import build_booking


@pytest.mark.integration
def test_booking_create_get_delete(restful_client, token_auth):
    """
    End-to-end: POST booking - GET booking - DELETE booking - Try to GET again.
    Use token for authentication.
    """
    # POST with custom data, verify response includes same data
    booking_payload = build_booking(
        fname="Alan",
        lname="Shepard",
        price=50,
        deposit=True,
        check_in="1961-05-05",
        check_out="1961-05-05",
        additional_needs="Orange juice, filet mignon wrapped in bacon, scrambled eggs.",
    )
    create_response_json = restful_client.create_booking(booking_payload).json()
    booking_id = create_response_json["bookingid"]
    for key, value in booking_payload.items():
        assert key in create_response_json["booking"]
        assert create_response_json["booking"][key] == value

    # GET and assert correct data
    get_response_json = restful_client.get_booking_by_id(booking_id=booking_id).json()
    for key, value in booking_payload.items():
        assert key in get_response_json
        assert get_response_json[key] == value

    # DELETE booking
    delete_response = restful_client.delete_booking_by_id(
        booking_id=booking_id, auth_header=token_auth
    )
    assert delete_response.status_code == 201

    # GET and assert booking is no longer found
    get_response = restful_client.get_booking_by_id(booking_id=booking_id)
    assert get_response.status_code == 404


@pytest.mark.integration
def test_booking_create_get_update(restful_client, api_key_auth):
    """
    End-to-end: POST booking - PATCH booking - Try to GET again.
    Use api key for authentication.
    """
    # POST with default data, verify response includes the same
    booking_payload = build_booking()
    create_response_json = restful_client.create_booking(payload=booking_payload).json()
    booking_id = create_response_json["bookingid"]
    for key, value in booking_payload.items():
        assert key in create_response_json["booking"]
        assert create_response_json["booking"][key] == value

    # PATCH booking with new first and last names
    update_payload = build_booking(partial=True, firstname="Yuri", lastname="Gagarin")
    patch_response_json = restful_client.update_booking_by_id(
        booking_id=booking_id,
        auth_header=api_key_auth,
        payload=update_payload,
        partial_update=True,
    ).json()

    # GET booking and verify first and last name were updated since creation
    get_response_json = restful_client.get_booking_by_id(booking_id=booking_id).json()
    assert (
        get_response_json["firstname"] != create_response_json["booking"]["firstname"]
    )
    assert get_response_json["lastname"] != create_response_json["booking"]["lastname"]
    assert get_response_json["firstname"] == patch_response_json["firstname"]
    assert get_response_json["lastname"] == patch_response_json["lastname"]
