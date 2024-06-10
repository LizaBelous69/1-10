import datetime as dt

# Замените 'YYYY, M, D, H, M' на реальные значения начала курса
start_moment = dt.datetime(2023, 1, 10, 9, 0)  # пример: 10 января 2023 года, 09:00 утра

# Текущий момент времени
current_moment = dt.datetime.now()

# Вычисляем разницу времени
total_time = current_moment - start_moment

print(total_time)
