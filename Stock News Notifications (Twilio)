import requests

# import time

from twilio.rest import Client

EQUITY_API_KEY = ''

NEWS_API_KEY = ''

EQUITY = "TSLA"

COMPANY_NAME = "Tesla Inc"

EQUITY_ENDPOINT_URL = 'https://www.alphavantage.co/query'

NEWS_ENDPOINT_URL = 'https://newsapi.org/v2/everything'

alpha_vantage_api_params = {

    'function': 'TIME_SERIES_DAILY',
    'symbol': EQUITY,
    'apikey': EQUITY_API_KEY
}

newsapi_params = {

    'q': COMPANY_NAME,
    'searchIn': 'title',
    'apiKey': NEWS_API_KEY
}

TWILIO_ACCOUNT_SID = ''

TWILIO_AUTH_TOKEN = ''

daily_time_series_response = requests.get(url=EQUITY_ENDPOINT_URL, params=alpha_vantage_api_params)
stock_price_data = daily_time_series_response.json()['Time Series (Daily)']

list_of_only_values = [value for (key, value) in stock_price_data.items()]

yesterday_closing_price = float(list_of_only_values[0]['4. close'])
day_before_yesterday_closing_price = float(list_of_only_values[1]['4. close'])

price_fluctuation = yesterday_closing_price - day_before_yesterday_closing_price
percentage = round((price_fluctuation/yesterday_closing_price) * 100)

up_down = None
if price_fluctuation < 0:
    up_down = '🔻'
else:
    up_down = '🔺'

if abs(percentage) > 5:

    news_response = requests.get(url=NEWS_ENDPOINT_URL, params=NEWS_API_KEY)
    article_list = news_response.json()[['articles']][:3]

    formatted_article_list = [f'{EQUITY}: {up_down}{percentage}%\nHeadline: {article["title"]}.'
                              f' \nBrief: {article["description"]}'
                              for article in article_list]

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    for article in formatted_article_list:

        message = client.messages \
            .create(
                body=article,
                from_='',
                to=''
        )

        print(message.sid)
