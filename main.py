# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv
birthday_date = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_date.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birth_day_name = ""
birth_day_email = ""

for birth in birthday_dict:
    if birth.get("month") == now.month and birth.get("day") == now.day:
        birth_day_name = birth.get("name")
        birth_day_email = birth.get("email")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter1:
            content = letter1.read()
            new_text = content.replace("[NAME]",birth_day_name)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birth_day_email,
                                msg="Subject:Happy Birthday!\n\n"
                                    f"{new_text}")

