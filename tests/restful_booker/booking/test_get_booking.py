import pytest

from resources.data_factories import booking_fields


def test_get_booking_by_valid_id(restful_client, valid_booking_id):
    """
    GET /booking/{id}, retrieve full booking details for a valid id.
    """
    response = restful_client.get_booking_by_id(booking_id=valid_booking_id)
    assert response.status_code == 200

    json_response = response.json()
    for field in booking_fields():
        if field in ["checkin", "checkout"]:
            assert field in json_response["bookingdates"]
        else:
            assert field in json_response


@pytest.mark.parametrize(
    "booking_id, expected_status",
    [
        (1, 200),
        (99999, 404),
        ("ten", 404),
        (None, 404),
    ],
    ids=["existing_id", "nonexistent_id", "invalid_id", "missing_id"],
)
def test_get_booking_by_id_variations(restful_client, booking_id, expected_status):
    """
    GET /booking/{id}, different id states.
    """
    response = restful_client.get_booking_by_id(booking_id=booking_id)
    assert response.status_code == expected_status


def test_get_all_booking_ids(restful_client):
    """
    GET /booking, should return list of booking ids.
    """
    response = restful_client.get_all_booking_ids()
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "query_params, status_code",
    [
        ({"firstname": "Jim"}, 200),
        ({"lastname": "Brown"}, 200),
        ({"firstname": "ThisPerson", "lastname": "DoesNotExist"}, 200),
        ({"invalidparam": "value"}, 200),
    ],
    ids=[
        "filter_by_firstname",
        "filter_by_lastname",
        "filter_no_matches",
        "invalid_query_key_ignored",
    ],
)
def test_get_booking_ids_with_query_params(restful_client, query_params, status_code):
    """
    GET /booking?query, test using various query filters.
    """
    response = restful_client.get_all_booking_ids(query_params=query_params)
    assert response.status_code == status_code
    list_of_bookings = response.json()

    if query_params == {"firstname": "Jim"}:
        for booking in list_of_bookings:
            booking_data = restful_client.get_booking_by_id(
                booking_id=booking["bookingid"]
            ).json()
            assert booking_data["firstname"] == "Jim"

    elif query_params == {"lastname": "Brown"}:
        for booking in list_of_bookings:
            booking_data = restful_client.get_booking_by_id(
                booking_id=booking["bookingid"]
            ).json()
            assert booking_data["lastname"] == "Brown"

    elif query_params == {"firstname": "ThisPerson", "lastname": "DoesNotExist"}:
        assert len(list_of_bookings) == 0

    elif query_params == {"invalidparam": "value"}:
        assert len(list_of_bookings) > 0
