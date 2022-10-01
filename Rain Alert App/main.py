import requests

from twilio.rest import Client

account_sid = 'AC4e679b8ab9199a40811114babf418edd'

auth_token = '3fcba1cef9eb94099d20f36f9dafb675'

api_key = 'c21ecfcf0b63e008dd049a5d309a9636'

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

MY_LAT = 53.144479
MY_LNG = -1.196703

api_parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=OWM_Endpoint, params=api_parameters)

response.raise_for_status()

weather_data = response.json()

hourly_slice = weather_data['hourly'][:12]

will_rain = False

for hourly_weather_dict in hourly_slice:
    condition_code = hourly_weather_dict['weather'][0]['id']

    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body="Bring an Umbrella (ella - ella)", from_='+19706654775', to='+4407759340651')

    print(message.status)


