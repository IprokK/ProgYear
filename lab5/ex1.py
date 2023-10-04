import requests

url = 'https://hh.ru'

headers = {
            'User-Agent': 'Chrome/58.0.3029.110'}

response = requests.get(url, headers=headers)
print(response.text)

