# Написать функцию, которая определяет какой сегодня день. Если выходной, то уведомляет об этом
from datetime import date


# weekday() возвращает число от 0 до 6, 0 - понедельник, а 6 - воскресенье
def date_today() -> str:
    date_full = date.today()
    date_day = date_full.weekday()
    date_array = {
        0: 'понедельник',
        1: 'вторник',
        2: 'среда',
        3: 'четверг',
        4: 'пятница',
        5: 'суббота',
        6: 'воскресенье',
    }
    return date_array[date_day]


if date_today() == 'суббота' or date_today() == 'воскресенье':
    print(f'Сегодня {date_today()}')
else:
    print(f'Сегодня {date_today()}')
