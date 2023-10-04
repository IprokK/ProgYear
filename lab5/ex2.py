import requests

def get_weather(city_name):
    api_key = '3b579dfb318460b8f4702992ebf5de2d'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': api_key}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        print(f'Погода в городе {city_name}:')
        print(f'Описание: {weather_description}')
        print(f'Влажность: {humidity}%')
        print(f'Давление: {pressure} hPa')
    else:
        print(f'Ошибка. Код: {response.status_code}')

city_name = input("Введите название города (Например: London, Moscow, Saint Petersburg: ")
get_weather(city_name)
