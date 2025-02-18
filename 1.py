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
    # Проверяем, что запрос равен 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':  
        friends_string = ''
        # Перебираем словарь DATABASE и добавляем имена друзей в переменную friends_string
        for friend in DATABASE:
            friends_string += friend + ' '
        # Возвращаем строку, составленную из 'Твои друзья: ' и friends_string 
        return 'Твои друзья: ' + friends_string
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
