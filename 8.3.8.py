DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'

def process_query(query):
    name, question = query.split(', ', 1)
    name = name.strip()  # Удаляем пробелы в начале и конце имени
    
    if name == 'Анфиса':
        if question.strip() == 'сколько у меня друзей?':
            count = len(DATABASE)
            return f'У тебя {format_friends_count(count)}.'
        elif question.strip() == 'кто все мои друзья?':
            friends_string = ', '.join(DATABASE)
            return f'Твои друзья: {friends_string}'
        elif question.strip() == 'где все мои друзья?':
            unique_cities = set(DATABASE.values())
            cities_string = ', '.join(unique_cities)
            return f'Твои друзья в городах: {cities_string}'
        else:
            return 'Извини, не поняла вас.'
    else:
        location = DATABASE.get(name)
        if location:
            return f'{name} в городе {location}.'
        else:
            return f'Извини, не знаю, где {name}.'

# Проверка
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Миша, ты где?'))
