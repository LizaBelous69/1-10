import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # Получаем город, где живет друг
    city = DATABASE.get(friend)
    if city is None:
        return "Друг не найден"
    
    # Получаем смещение от UTC для указанного города
    offset = UTC_OFFSET.get(city)
    if offset is None:
        return "Город не найден"
    
    # Получаем текущее время в UTC
    current_utc_time = dt.datetime.utcnow()
    
    # Вычисляем текущее время в указанном городе
    local_time = current_utc_time + dt.timedelta(hours=offset)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

print(what_time('Соня'))
