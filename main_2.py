import requests

from datetime import datetime

import smtplib

MY_LAT = 51.507351
MY_LONG = -0.127758

my_gmail = "ogamwtomounithspanagias@gmail.com"
my_gmail_password = "opkodikos12"

my_yahoo_email = 'pan_pan37@yahoo.com'
sending_from_yahoo_password = 'iyqzymdfwudgdojh'


def above():

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def visible():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


if visible and above():

    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_gmail_password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_yahoo_email, msg='Subject: Look Up\n\nLook Up Now!')
