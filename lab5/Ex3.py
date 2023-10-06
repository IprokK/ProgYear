import requests
import json

# Вариант №4 (т.к. у hh.ru долгая процедура получения API)


def get_news(country='ru', category='technology', page_size=5):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {'country': country,
              'category': category,
              'pageSize': page_size,
              'apiKey': '5f338837a2104713b2fec3f687a941ea'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        print(f'Топ {page_size} новостей в категории {category} для страны {country}:')
        for index, article in enumerate(data['articles'], 1):
            print(f"Новость {index}:")
            print(f"Заголовок: {article['title']}")
            print(f"Описание: {article['description']}")
            print(f"Источник: {article['source']['name']}")
            print(f"Опубликовано: {(article['publishedAt']).split('T')[0] + ' ' + (article['publishedAt']).split('T')[1][:-1]}")
            print(f"Ссылка: {article['url']}")
            print("----------")
    else:
        print(f'Ошибка. Код: {response.status_code}')


get_news()
