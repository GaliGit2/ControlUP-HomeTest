import requests

from HomeTest.config import API_BASE_URL, DISTANCE_URL, \
    ITEMS_COUNT_EXCEPTION, ITEMS_MISSING_EXCEPTION, MIN_EXPECTED_DISTANCE_KM, DISTANCE_TOO_SMALL_EXCEPTION, \
    EXPECTED_AIRPORTS_COUNT, EXPECTED_AIRPORTS, AIRPORT_1, AIRPORT_2, NAME, DISTANCE_KM, \
    RESPONSE_MISSING_KILOMETERS_EXCEPTION, AIRPORTS, ATTRIBUTES, DESTINATION, DEPARTURE

#API Tests

def get_airports():
    response = requests.get(API_BASE_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    airports = data.get(AIRPORTS, [])
    return airports

#Scenario 1: Verify Airport Count
def test_airports_count():
    airports = get_airports()
    assert len(airports) == EXPECTED_AIRPORTS_COUNT, (
        f"{ITEMS_COUNT_EXCEPTION}: Expected {EXPECTED_AIRPORTS_COUNT}, got {len(airports)}"
    )

#Scenario 2: Verify Specific Airports
def test_expected_airports_present():
    airports = get_airports()
    airports_names = {airport.get(ATTRIBUTES, {}).get(NAME) for airport in airports}
    missing_airports = EXPECTED_AIRPORTS - airports_names
    assert not missing_airports, f"{ITEMS_MISSING_EXCEPTION}: {missing_airports}"

#Scenario 3: Verify Distance Between Airports
def test_airports_distance():
    payload = {DESTINATION: AIRPORT_1, DEPARTURE: AIRPORT_2}
    response = requests.post(DISTANCE_URL, json=payload)
    response.raise_for_status()
    result = response.json()

    distance = result.get(AIRPORTS, {}).get(ATTRIBUTES, {}).get(DISTANCE_KM)
    assert distance is not None, RESPONSE_MISSING_KILOMETERS_EXCEPTION
    assert distance > MIN_EXPECTED_DISTANCE_KM, (
        f"{DISTANCE_TOO_SMALL_EXCEPTION}: got {distance} km"
    )