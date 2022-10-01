import os

from twilio.rest import Client

import smtplib

TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_VIRTUAL_NUMBER = ''
TWILIO_VERIFIED_NUMBER = ''

my_email = ''
my_password = ''

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):

        message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER
            )

        print(message.sid)

    def send_emails(self, text, emails, google_flight_link):

        with smtplib.SMTP(host='smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            for email in emails:
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!"
                                        f"\n\n{text}\n{google_flight_link}".encode('utf-8'))

