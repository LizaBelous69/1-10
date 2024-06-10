DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':  
        friends_string = ''
        for friend in DATABASE:
            friends_string += friend + ' '
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        # Создаем список всех городов из словаря DATABASE
        cities = list(DATABASE.values())
        # Удаляем повторяющиеся города, оставляем только уникальные
        unique_cities = list(set(cities))
        # Формируем строку с перечислением городов
        cities_string = ' '.join(unique_cities)
        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'

# Проверяем
print(process_anfisa('Где все мои друзья?'))
