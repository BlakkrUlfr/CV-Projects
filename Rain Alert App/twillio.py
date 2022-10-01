# Download the helper library from https://www.twilio.com/docs/python/install
import os

from twilio.rest import Client

from twilio.http.http_client import TwilioHttpClient

# Find your Account SID and Auth Token at twilio.com/console
# and set the Environment Variables. See http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='',
                     to=''
                 )

print(message.sid)

from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = 'your account id here'
auth_token = 'your twilio token here'

client = Client(account_sid, auth_token, http_client=proxy_client)

# twilio api calls will now work from behind the proxy:
message = client.messages.create(to="...", from_='...', body='...')
