from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

# ----------------------------- SEARCH IATACODE -----------------------------
# Do an if statement so you don't have to call sheety API every single time :)), tricky but may prone to some errors.
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

# ----------------------------- HARDCODE DATA TO TEST OUT -----------------------------
# sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
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

for row in sheet_data:
    search_result = FlightSearch().check_flights(origin_city_code="LON",
                                                 destination_city_name=row["city"],
                                                 destination_city_code=row["iataCode"],
                                                 from_time=tomorrow,
                                                 to_time=one_year_from_tomorrow)
    if search_result is not None:
        if search_result.price < row["lowestPrice"]:
            NotificationManager().send_notification(search_result)
