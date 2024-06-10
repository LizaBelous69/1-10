import urllib.parse

user_query = 'как стать бэкенд-разработчиком'
encoded_query = urllib.parse.quote(user_query)

url = f'https://yandex.ru/search/?text={encoded_query}'

print(url)
