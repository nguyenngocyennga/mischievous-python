# Stock Trading News Alert Project

from key import ALPHA_VANTAGE_API_KEY, NEWS_API_KEY
from key import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_NUMBER
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

# Get stock data
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

response = requests.get(ALPHA_VANTAGE_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_data = float(data_list[0]["4. close"])
before_yesterday_closing_data = float(data_list[1]["4. close"])

# Compare stock data
difference = yesterday_closing_data - before_yesterday_closing_data
percentage_difference = abs(difference) / yesterday_closing_data * 100
up_down = None
if difference >= 0:
    up_down = f"🔺{round(percentage_difference)}%"
else:
    up_down = f"🔻{round(percentage_difference)}%"

# Get top news
if percentage_difference >= 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url=NEWS_API_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()["articles"][:3]
    formatted_news = [f"{COMPANY_NAME} {up_down}\nHEADLINE: {item['title']}\nBRIEF: {item['description']}" for item in news_data]
    # print(news_data)

    # Send sms alert
    for article in formatted_news:
        # print(article)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=article,
                from_=TWILIO_PHONE_NUMBER,
                to=RECIPIENT_NUMBER
            )
