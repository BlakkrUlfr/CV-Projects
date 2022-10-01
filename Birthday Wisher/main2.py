from datetime import datetime

import pandas

import random

import smtplib

my_gmail = ""
my_gmail_password = ""

my_yahoo_email = ''
sending_from_yahoo_password = ''

today = (datetime.now().month, datetime.now().day)

bday_data = pandas.read_csv(filepath_or_buffer='birthdays.csv')

birthday_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in bday_data.iterrows()
}

print(birthday_dict)

if today in birthday_dict:

    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'

    birthday_person = birthday_dict[today]

    with open(file=file_path, mode='r') as letter:
        content = letter.read()
        wish = content.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_gmail_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday\n\n{wish}"
        )
