# API Endpoints & API Parameters - ISS Overhead Notifier

import requests
from datetime import datetime
from account_info import my_email, my_password, recipient
import smtplib
from time import sleep

MY_LAT = 21.044660
MY_LONG = 105.842360


def is_your_location_under_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    sunrise_sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_sunset_response.raise_for_status()
    data = sunrise_sunset_response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now or time_now <= sunrise:
        return True


while True:
    sleep(60)
    if is_your_location_under_iss() and is_night():
        print("yes it's near")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient,
                                msg="Subject: Look up!\n\nISS is above you!")
    else:
        print("Nope, so far away")
