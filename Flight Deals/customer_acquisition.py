import requests

acquisition_sheety_endpoint = 'https://api.sheety.co/fb3565f6afb850bcc0d52f5d10622f08/flightDeals/users'
BEARER_TOKEN = ''
sheety_headers = {

    'Authorization': f'Bearer {BEARER_TOKEN}'
}


def customer_acquisition():
    print("Welcome to Pan's Flight Club")
    print("We find the best flight deals and email you")
    first_name = str(input('What is your first name?')).upper()
    last_name = str(input('What is your last name?')).upper()
    email = str(input('What is your email?'))
    email_verification = str(input('Type your email again.'))

    sheety_acquisition_params = {

        'user': {

            'First Name': first_name,
            'Last Name': last_name,
            'Email': email_verification

        }
    }

    if email == email_verification:
        acquisition_response = requests.put(url=acquisition_sheety_endpoint,
                                            json=sheety_acquisition_params,
                                            headers=sheety_headers)
        print(acquisition_response.text)
        print('You are in the club')


customer_acquisition()
