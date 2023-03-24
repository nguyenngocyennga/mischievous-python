# Automated Amazon Price Tracker

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from key import EMAIL, PASSWORD, RECIPIENT

# url = "https://www.amazon.com/Instant-Pot-Electric-Pressure-Stainless/dp/B081Z9FKDB/ref=dp_fod_1?pd_rd_i=B081Z9FKDB&psc=1"
url = "https://www.amazon.com/dp/B091TTDRVP/"
header = {
    "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
