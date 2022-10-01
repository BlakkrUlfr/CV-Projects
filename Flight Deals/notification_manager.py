import os

from twilio.rest import Client

import smtplib

TWILIO_SID = 'AC4e679b8ab9199a40811114babf418edd'
TWILIO_AUTH_TOKEN = '3fcba1cef9eb94099d20f36f9dafb675'
TWILIO_VIRTUAL_NUMBER = '+19706654775'
TWILIO_VERIFIED_NUMBER = '07759340651'

my_email = 'ogamwtomounithspanagias@gmail.com'
my_password = 'opkodikos12'

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

