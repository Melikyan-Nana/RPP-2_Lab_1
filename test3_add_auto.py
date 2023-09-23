import requests

url = 'http://127.0.0.1:5000/v1/add/auto'

data = {
    'city_id': 54,
    'name': 'BMW X3',
    'horse_power': 190,
    'production_year': 2022
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
