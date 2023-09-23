import requests

url = 'http://127.0.0.1:5000/v1/add/region'

data = {
    'id': 54,
    'name': 'Новосибирская область'
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
