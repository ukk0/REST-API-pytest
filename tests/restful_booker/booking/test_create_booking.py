import pytest

from resources.data_factories import build_booking


@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking_valid(restful_client):
    """
    POST /booking, create new booking with valid payload.
    """
    booking_payload = build_booking(additional_needs="Coffee")
    response = restful_client.create_booking(payload=booking_payload)
    assert response.status_code == 200

    json_response = response.json()
    assert "bookingid" in json_response
    for k in json_response["booking"]:
        assert booking_payload[k] == json_response["booking"][k]


@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking_missing_payload(restful_client):
    """
    POST /booking, missing payload in request should cause fail.
    """
    response = restful_client.create_booking(payload=None)
    assert response.status_code == 500


@pytest.mark.regression
@pytest.mark.parametrize(
    "fname, lname, price, deposit_paid",
    [
        (None, "McTester", 100, True),
        ("Testy", None, 100, True),
        ("Testy", "McTester", None, True),
        ("Testy", "McTester", 100, None),
    ],
    ids=["missing_fname", "missing_lname", "missing_price", "missing_deposit"],
)
def test_create_booking_missing_required_values(
    restful_client, fname, lname, price, deposit_paid
):
    """
    POST /booking, create booking with missing required values or wrong datatype should fail.
    """
    booking_payload = build_booking(
        fname=fname, lname=lname, price=price, deposit=deposit_paid
    )
    response = restful_client.create_booking(payload=booking_payload)
    assert response.status_code == 500


@pytest.mark.regression
@pytest.mark.parametrize(
    "field_to_remove",
    ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"],
    ids=[
        "missing_fname",
        "missing_lname",
        "missing_price",
        "missing_deposit",
        "missing_dates",
    ],
)
def test_create_booking_invalid_payloads(restful_client, field_to_remove):
    """
    POST /booking, invalid payloads missing a field entirely should fail.
    """
    booking_payload = build_booking()
    del booking_payload[field_to_remove]

    response = restful_client.create_booking(payload=booking_payload)
    assert response.status_code == 500
