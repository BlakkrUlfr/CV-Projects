import json

from pprint import pprint

import requests

from flight_data import FlightData

TEQUILA_API_KEY = 'dWwXQmpPck3LoeT20_cUhOEzjN2pe4pB'
tequila_endpoint = 'https://tequila-api.kiwi.com/v2/search'

location_endpoint = f"{tequila_endpoint}/locations/query"
search_endpoint = f"{tequila_endpoint}/v2/search"

tequila_headers = {

    'apikey ': TEQUILA_API_KEY
}


class FlightSearch:

    def get_destination_code(self, city_name):

        query = {

            'term ': city_name,
            'location_types': 'city'
        }
        response = requests.get(url=location_endpoint, headers=tequila_headers, params=query)

        try:
            results = response.json()["locations"]
            code = results[0]["code"]
            return code
        except json.decoder.JSONDecodeError:
            print('The responses can be gzipped, if request header accept-encoding:gzip, '
                  'and need to be unpacked if response header is Content-Encoding: gzip ')

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=search_endpoint, headers=tequila_headers, params=query)

        try:
            check_flight_data = response.json()["data"][0]

        except json.decoder.JSONDecodeError:
            print('The responses can be gzipped, if request header accept-encoding:gzip, '
                  'and need to be unpacked if response header is Content-Encoding: gzip ')

        except IndexError:

            query["max_stopovers"] = 1

            response = requests.get(url=f"{search_endpoint}/v2/search", headers=tequila_headers, params=query)
            check_flight_data = response.json()["data"][0]

            pprint(check_flight_data)

            flight_data = FlightData(
                price=check_flight_data["price"],
                origin_city=check_flight_data["route"][0]["cityFrom"],
                origin_airport=check_flight_data["route"][0]["flyFrom"],

                destination_city=check_flight_data["route"][1]["cityTo"],
                destination_airport=check_flight_data["route"][1]["flyTo"],

                out_date=check_flight_data["route"][0]["local_departure"].split("T")[0],

                return_date=check_flight_data["route"][2]["local_departure"].split("T")[0],

                stop_overs=1,

                via_city=check_flight_data["route"][0]['cityTo']
            )
            return flight_data

        else:
            flight_data = FlightData(
                price=check_flight_data["price"],
                origin_city=check_flight_data["route"][0]["cityFrom"],
                origin_airport=check_flight_data["route"][0]["flyFrom"],
                destination_city=check_flight_data["route"][0]["cityTo"],
                destination_airport=check_flight_data["route"][0]["flyTo"],
                out_date=check_flight_data["route"][0]["local_departure"].split("T")[0],
                return_date=check_flight_data["route"][1]["local_departure"].split("T")[0]
                )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
