import requests
from HomeTest.config import API_BASE_URL, DEFAULT_TIMEOUT, AIRPORTS, ATTRIBUTES, NAME, DEPARTURE, \
    DESTINATION, DISTANCE_URL, DISTANCE_KM

def get_airports():
    response = requests.get(API_BASE_URL, timeout=DEFAULT_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    airports = data.get(AIRPORTS, [])
    return airports

def get_airports_count():
    return len(get_airports())

def get_missing_airports(expected_airports):
    airports_names = {airport.get(ATTRIBUTES, {}).get(NAME) for airport in get_airports()}
    return expected_airports - airports_names

def get_distance_between_airports(airport1, airport2):
    payload = {DEPARTURE: airport1, DESTINATION: airport2}
    response = requests.post(DISTANCE_URL, json=payload)
    response.raise_for_status()
    result = response.json()
    return result.get(AIRPORTS, {}).get(ATTRIBUTES, {}).get(DISTANCE_KM)