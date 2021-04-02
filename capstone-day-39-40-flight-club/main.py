from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

destination_data = data_manager.get_destination_data()
email_list = data_manager.get_email_list()
# ----------------------------- SEARCH IATACODE -----------------------------
# Do an if statement so you don't have to call sheety API every single time :)), tricky but may prone to some errors.
if destination_data[0]["iataCode"] == "":
    for destination in destination_data:
        destination["iataCode"] = flight_search.get_destination_code(destination["city"])
    data_manager.destination_data = destination_data
    data_manager.update_destination_data()

# ----------------------------- HARDCODE DATA TO TEST OUT -----------------------------
# destination_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
#  {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},
#  {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
#  {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
#  {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
#  {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
#  {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378},
#  {'city': 'Chengdu', 'iataCode': 'CTU', 'id': 11, 'lowestPrice': 89},
#  {'city': 'Phuket', 'iataCode': 'HKT', 'id': 12, 'lowestPrice': 89},
#  {'city': 'Shanghai', 'iataCode': 'SHA', 'id': 13, 'lowestPrice': 98}]

# ----------------------------- SEARCH CHEAP FLIGHTS -----------------------------
today = datetime.today().date()
tomorrow = (today + timedelta(days=1)).strftime("%d/%m/%Y")
one_year_from_tomorrow = (today + timedelta(days=(30*12))).strftime("%d/%m/%Y")

for destination in destination_data:
    flight = flight_search.check_flights(origin_city_code=ORIGIN_CITY_CODE,
                                         destination_city_name=destination["city"],
                                         destination_city_code=destination["iataCode"],
                                         from_time=tomorrow,
                                         to_time=one_year_from_tomorrow)
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        price_formatted = "{:,}".format(flight.price)
        message = f"Low price alert! Only ${price_formatted} to fly " \
                  f"from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."
        google_flight_link = f"\nhttps://www.google.co.uk/flights?hl=en#flt=" \
                             f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}" \
                             f"*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_sms(message)
        for user in email_list:
            email_body = message + google_flight_link
            # name = user["firstName"] + user["lastName"]
            email_address = user["email"]
            notification_manager.send_email(email_address, email_body)
        print(email_list)
