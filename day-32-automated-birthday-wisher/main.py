# Send Email (smtplib) and Manage Dates (datetime)

from account_info import my_email, my_password
from datetime import datetime
import smtplib
import random
import pandas

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    letter_file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_file_path) as letter_file:
        content = letter_file.read()
        name = birthdays_dict[today]["name"]
        address_to_send = birthdays_dict[today]["email"]
        letter_to_send = content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=address_to_send,
                            msg=f"Subject: Happy Birthday!"
                                f"\n\n{letter_to_send}")
