import requests

api_parameters = {
    'amount': 20,
    'type': 'boolean',
    'category': 18,
}

response = requests.get(url='https://opentdb.com/api.php?', params=api_parameters)

response.raise_for_status()
data = response.json()

trivia_questions = data['results']
