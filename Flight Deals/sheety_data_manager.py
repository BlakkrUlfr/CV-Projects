import requests
from pprint import pprint

sheety_endpoint = 'https://api.sheety.co/fb3565f6afb850bcc0d52f5d10622f08/flightDeals/prices'
BEARER_TOKEN = ''

sheety_endpoint_users = 'https://api.sheety.co/fb3565f6afb850bcc0d52f5d10622f08/flightDeals/users'

sheety_headers = {

    'Authorization': f'Bearer {BEARER_TOKEN}'
}


class DataManager:

    def __init__(self):
        self.sheety_destination_data = []
        self.sheety_customer_data = []

    def get_destination_data(self):

        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        sheety_response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        sheety_data = sheety_response.json()
        self.sheety_destination_data = sheety_data["prices"]

        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        pprint(self.sheety_destination_data)
        return self.sheety_destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):

        for nested_dict in self.sheety_destination_data:

            sheety_temp_dict = {
                "price": {
                    "iataCode": nested_dict["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{nested_dict['id']}",
                                    json=sheety_temp_dict, headers=sheety_headers)
            print(response.text)

    def get_customers_emails(self):

        sheety_response = requests.get(url=sheety_endpoint_users, headers=sheety_headers)
        sheety_data = sheety_response.json()
        self.sheety_customer_data = sheety_data["users"]
        return self.sheety_customer_data



