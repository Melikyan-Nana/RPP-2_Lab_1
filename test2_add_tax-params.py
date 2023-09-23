import requests

url = 'http://127.0.0.1:5000/v1/add/tax-param'

data = {
    'city_id': 54,
    'from_hp_car': 150,
    'to_hp_car': 200,
    'from_production_year_car': 2022,
    'to_production_year_car': 2023,
    'rate': 5
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
