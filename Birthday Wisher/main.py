import pandas

import datetime as dt

import random

import smtplib

csv_data = pandas.read_csv(filepath_or_buffer='birthdays.csv')

my_gmail = "ogamwtomounithspanagias@gmail.com"
my_gmail_password = "opkodikos12"

my_yahoo_email = 'pan_pan37@yahoo.com'
sending_from_yahoo_password = 'iyqzymdfwudgdojh'

name_placeholder = '[NAME]'

file_path_list = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

now = dt.datetime.now()
month = now.month
day = now.day

for (index, row) in csv_data.iterrows():

    if row.month == month and row.day == day:

        # Replace name with test_name in birthdays.csv

        random_letter = random.choice(file_path_list)
        with open(file=random_letter, mode='r') as letter:
            text = letter.read()
            complete_letter = text.replace(name_placeholder, row.name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=my_gmail_password)
                connection.sendmail(
                    from_addr=my_gmail,
                    to_addrs=row.email,
                    msg=f"Subject:Happy Birthday\n\n{complete_letter}"
                )

