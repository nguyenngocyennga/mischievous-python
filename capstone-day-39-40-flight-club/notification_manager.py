from key import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_NUMBER
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, search_result):
        # print(type(search_result))
        price_formatted = "${:,}".format(search_result.price)
        sms_content = f"Low price alert! Only {price_formatted} to fly " \
                      f"from {search_result.origin_city}-{search_result.origin_airport} " \
                      f"to {search_result.destination_city}-{search_result.destination_airport}, " \
                      f"from {search_result.out_date} to {search_result.return_date}."
        # print(sms_content)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=sms_content,
                from_=TWILIO_PHONE_NUMBER,
                to=RECIPIENT_NUMBER
            )
