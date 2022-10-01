import requests

import json

TEQUILA_API_KEY = 'dWwXQmpPck3LoeT20_cUhOEzjN2pe4pB'
tequila_endpoint = 'https://tequila-api.kiwi.com/v2/search'

location_endpoint = f"{tequila_endpoint}/locations/query"

tequila_headers = {

    'apikey ': TEQUILA_API_KEY
}

query = {

    'term ': 'Athens',
    'location_types': 'city'
}
response = requests.get(url=location_endpoint, headers=tequila_headers, params=query)
results = response.json()["locations"]
code = results[0]["code"]
print(code)

head = requests.head(url=location_endpoint)

header = head.headers

contentType = header.get('content-type')

print(contentType)
