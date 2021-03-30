from password import my_email, my_password, recipient
import smtplib
import datetime as dt  # shorten datetime module
import random

now = dt.datetime.now()
current_date_of_week = now.weekday()

if current_date_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        to_send_quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_password, to_addrs=recipient,
                            msg=f"Subject: Hourly message for you :-)"
                                f"\n\n{to_send_quote}")

# ------------------------- CLASS NOTES ---------------------------------
# # Location of email provider SMTP server
# connection = smtplib.SMTP("smtp.gmail.com")
# connection. starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="nganguyen.ny@gmail.com",
#     msg=""
#         "Subject:Hello"
#         "\n\nTalking to myself, again.")
# connection.close()

# # Get to 'datetime' class, method 'now()' get you current date & time
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()  # Start from 0
# print(day_of_week)
#
# # Create your own datetime object
# date_of_birth = dt.datetime(year=1961, month=3, day=1, hour=4, minute=39)
# print(date_of_birth)

# # Or use 'with'
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="nganguyen.ny@gmail.com",
#         msg=""
#             "Subject:Hello"
#             "\n\nTalking to myself, again.")
