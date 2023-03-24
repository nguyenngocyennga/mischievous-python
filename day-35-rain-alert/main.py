# Keys, Authentication, Environment Variables: Send SMS

import os
from key import api_key, twilio_phone_number, recipient_number, twilio_account_sid, twilio_auth_token
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from datetime import datetime

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": 21.027763,
    "lon": 105.834160,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWN_Endpoint, params=parameters)
response.raise_for_status()
hourly_weather_data = response.json()["hourly"][:12]

will_rain = False

for hour in hourly_weather_data:
    for i in hour["weather"]:
        if i["id"] < 700:
            will_rain = True
        else:
            will_rain = False

# Use proxy to connect PythonAnywhere with Twilio to schedule SMS alert
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(twilio_account_sid, twilio_auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's gonna rain today. Bring your umbrelaaahh! ☔️",
            from_=twilio_phone_number,
            to=recipient_number
        )

    print(message.status)
