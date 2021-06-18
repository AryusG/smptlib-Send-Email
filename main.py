import smtplib
import datetime as dt
import random

# Variables
my_email = "weirdnthings@gmail.com"
my_password = "Konoha1345"
garox_email = "garox.lee.gl@gmail.com"

time = dt.datetime.now()
weekday = time.weekday()

with open("quotes.txt", newline='') as data_file:
    all_quotes = data_file.readlines()
    quote = random.choice(all_quotes)

if weekday == 4:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=garox_email,
                            msg=f"Subject: Sup bitch\n\n{quote}")


