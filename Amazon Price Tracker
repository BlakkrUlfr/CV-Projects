import requests

# import lxml

from bs4 import BeautifulSoup

import smtplib

url = "https://www.amazon.com/EIELO-Stainless-Spinning-Anxiety-Engagement/dp/B08RB16G41/ref=sr_1_25?crid=163P5ZCXPXJRV" \
      "&keywords=rings+for+men&qid=1658344839&sprefix=rings%2Caps%2C225&sr=8-25"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=url, headers=headers)
webpage = response.content

soup = BeautifulSoup(markup=webpage, features="lxml")
# print(soup.prettify())

price = soup.find(name='span', class_='a-offscreen').getText()

price_without_currency = price.split(sep='$')[1]

price_as_float = float(price_without_currency)

title = soup.find(id='productTitle').getText().strip()

target_price = 15
if price_as_float < target_price:
    message = f"{title} is now {price_as_float}"
    app_password = 'riyzawisuqqjhdol'

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()

        try:
            result = connection.login("pantelis.kaliviotis@gmail.com", app_password)
            connection.sendmail(
                from_addr="pantelis.kaliviotis@gmail.com",
                to_addrs="ogamwtomounithspanagias@gmail.com",
                msg=f"Subject:Amazon Price Alert!\n\n{message.encode('utf-8')}\n{price_as_float}\n{url}"
            )
        except smtplib.SMTPAuthenticationError:
            print('WTF')


















