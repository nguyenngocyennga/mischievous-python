from key import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_NUMBER
from key import MY_EMAIL, MY_PASSWORD
from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, info_message):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=info_message,
                from_=TWILIO_PHONE_NUMBER,
                to=RECIPIENT_NUMBER
            )
        print(message)

    def send_email(self, email_address, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email_address,
                msg=f"Subject: New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )
