from HomeTest.config import MIN_EXPECTED_DISTANCE_KM, DISTANCE_TOO_SMALL_EXCEPTION, \
    EXPECTED_AIRPORTS_COUNT, EXPECTED_AIRPORTS, AIRPORT_1, AIRPORT_2,\
    RESPONSE_MISSING_KILOMETERS_EXCEPTION, AIRPORTS_MISSING_EXCEPTION, AIRPORTS_COUNT_EXCEPTION
from HomeTest.helpers.api_helpers import get_airports_count, get_missing_airports, get_distance_between_airports


#API Tests

#Scenario 1: Verify Airport Count
def test_airports_count():
    airports_count = get_airports_count()
    assert airports_count == EXPECTED_AIRPORTS_COUNT, (
        f"{AIRPORTS_COUNT_EXCEPTION}: Expected {EXPECTED_AIRPORTS_COUNT}, got {airports_count}"
    )

#Scenario 2: Verify Specific Airports
def test_expected_airports_present():
    missing_airports = get_missing_airports(EXPECTED_AIRPORTS)
    assert not missing_airports, f"{AIRPORTS_MISSING_EXCEPTION}: {missing_airports}"

#Scenario 3: Verify Distance Between Airports
def test_airports_distance():
    distance = get_distance_between_airports(AIRPORT_1, AIRPORT_2)
    assert distance is not None, RESPONSE_MISSING_KILOMETERS_EXCEPTION
    assert distance > MIN_EXPECTED_DISTANCE_KM, (
        f"{DISTANCE_TOO_SMALL_EXCEPTION}: got {distance} km"
    )