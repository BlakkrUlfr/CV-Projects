import requests

from datetime import datetime

import os

APP_ID = os.environ['APP_ID']

NUTRITIONIX_API_KEY = os.environ['NUTRITIONIX_API_KEY']

GENDER = 'male'
WEIGHT_KG = 83
HEIGHT_CM = 177
AGE = 29

BEARER_TOKEN = os.environ['BEARER_TOKEN']

exercise_text = input("Tell me which exercises you did: ")

natural_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutritionix_headers = {

    'x-app-id': APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}

natural_exercise_params = {

    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

natural_exercise_response = requests.post(natural_exercise_endpoint, json=natural_exercise_params,
                                          headers=nutritionix_headers)
natural_exercise_result = natural_exercise_response.json()
print(natural_exercise_result)

sheety_endpoint = os.environ['sheety_endpoint']
today = datetime.now()
formatted_date = today.date().strftime('%d/%m/%y')
formatted_time = today.time().strftime('%X')

bearer_headers = {

    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in natural_exercise_result['exercises']:

    sheet_params = {

        "workout": {

            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_params, headers=bearer_headers)
    print(sheet_response.text)

