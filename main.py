import requests

from datetime import datetime

USERNAME = 'idkwhat2type'
TOKEN = 'Opkodikos12!'
GRAPH_ID = 'graph0'

request_header = {

    'X-USER-TOKEN': TOKEN
}

pixela_endpoint_url = 'https://pixe.la/v1/users'

create_user_params = {

    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# post_response_user = requests.post(url=pixela_endpoint_url, json=create_user_params)
# print(post_response_user.text)

graph_endpoint_url = f'{pixela_endpoint_url}/{USERNAME}/graphs'

graph_config_params = {

    'id': 'graph0',
    'name': 'Coding Graph',
    'unit': 'Hour',
    'type': 'float',
    'color': 'shibafu'
}

# post_response_graph = requests.post(url=graph_endpoint_url, json=graph_config_params, headers=request_header)
# print(post_response_graph.text)

pixel_creation_endpoint_url = f'{pixela_endpoint_url}/{USERNAME}/graphs/{GRAPH_ID}'

day_specified = datetime.now()

post_value_params = {

    'date': day_specified.strftime('%Y%m%d'),
    'quantity': input('How many hours did you Code today?')
}

post_response_pixel_creation = requests.post(url=pixel_creation_endpoint_url, json=post_value_params,
                                             headers=request_header)
print(post_response_pixel_creation.text)

# update_day = '20220519'
day_to_update = datetime(year=2022, month=5, day=19)
day_to_update.strftime('%Y%m%d')

pixel_update_delete_endpoint_url = f'{pixela_endpoint_url}/{USERNAME}/graphs/{GRAPH_ID}' \
                                   f'/{day_to_update.strftime("%Y%m%d")}'

put_value_params = {

    'quantity': input('Your Update:')
}

# put_response_value = requests.put(url=pixel_update_endpoint_url, json=put_value_params, headers=request_header)
# print(put_response_value.text)

# delete_response_value = requests.delete(url=pixel_update_delete_endpoint_url, headers=request_header)
# print(delete_response_value.text)

