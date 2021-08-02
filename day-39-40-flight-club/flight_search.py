import requests
from key import TEQUILA_KIWI_API_KEY
from flight_data import FlightData
from pprint import pprint

TEQUILA_KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_KIWI_HEADERS = {
    "apikey": TEQUILA_KIWI_API_KEY,
    "Content-Encoding": "gzip"
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # code = "TESTING"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_KIWI_ENDPOINT}/locations/query", params=params, headers=TEQUILA_KIWI_HEADERS)
        data = response.json()["locations"]
        city_code = data[0]["code"]
        return city_code

    def check_flights(self, origin_city_code, destination_city_name, destination_city_code, from_time, to_time):
        booking_token = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": from_time,
            "dateTo": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "USD",
            # "price_to": row["lowestPrice"],
            "max_stopovers": 0,
            # "sort": "price",
            "one_for_city": 1
        }
        response = requests.get(url=f"{TEQUILA_KIWI_ENDPOINT}/v2/search",
                                params=booking_token, headers=TEQUILA_KIWI_HEADERS)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found to {destination_city_name} ({destination_city_code})")
            return None

        new_flight = FlightData(
            price=int(data["price"]),
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        price_formatted = "{:,}".format(new_flight.price)
        print(f"From {new_flight.origin_city} to {new_flight.destination_city}: ${price_formatted} "
              f"Date: {new_flight.out_date} - {new_flight.return_date}")
        return new_flight
