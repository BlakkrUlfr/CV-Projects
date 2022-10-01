from datetime import datetime, timedelta

from flight_search import FlightSearch

from sheety_data_manager import DataManager

from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

sheety_data_manager = DataManager()

flight_search = FlightSearch()

notification_manager = NotificationManager()

sheetier_data = sheety_data_manager.get_destination_data()

if sheetier_data[0]["iataCode"] == "":

    for row_dict in sheetier_data:
        row_dict["iataCode"] = flight_search.get_destination_code(row_dict["city"])
    print(f"sheetier_data:\n {sheetier_data}")

    sheety_data_manager.sheety_destination_data = sheetier_data
    sheety_data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheetier_data:

    flight_info = flight_search.check_flights(origin_city_code=ORIGIN_CITY_IATA,
                                              destination_city_code=destination["iataCode"],
                                              from_time=tomorrow, to_time=six_month_from_today)

    if flight_info is None:
        continue

    if flight_info.price < destination["lowestPrice"]:

        sheety_users_data = sheety_data_manager.get_customers_emails()

        emails = [row['email'] for row in sheety_users_data]
        first_names = [row['firstName'] for row in sheety_users_data]

        text = f"Low price alert! Only £{flight_info.price}"
        f"to fly from {flight_info.origin_city}-{flight_info.origin_airport}"
        f"to {flight_info.destination_city}-{flight_info.destination_airport},"
        f"from {flight_info.out_date} to {flight_info.return_date}."

        if flight_info.stop_overs > 0:
            text += f"\nFlight has {flight_info.stop_overs} stop over, via {flight_info.via_city}."
            print(text)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight_info.origin_airport}" \
               f".{flight_info.destination_airport}" \
               f".{flight_info.out_date}*{flight_info.destination_airport}" \
               f".{flight_info.origin_airport}.{flight_info.return_date}"

        notification_manager.send_sms(message=text)
        notification_manager.send_emails(text=text, emails=emails, google_flight_link=link)


