# Задание:
# Составьте массив словарей с 6 билетами на поезд.
# Ключ в словаре — место пассажира в вагоне.
# Затем выведите все билеты на экран через цикл.
# Так же добавьте возможно создавать билет пользователя, спрашивая данные:
# Маршрут,
# Фамилия и инициалы пассажира,
# Данные паспорта,
# Номер билета должен создаваться автоматически. Например, сейчас билетов всего 2 ( билет 1 с номером 1, билет 2 с
# номером 2),
# значит следующий билет должен быть с номером 3.
# https://i.imgur.com/6D9dgBR.png

import random

from .consts import id_route_mapping


def base_append(base, place_key, ticket_number, route_name, username_fio, passport_details):
    base[place_key] = [ticket_number, route_name, username_fio, passport_details]


def base_print(base):
    for key, values in base.items():
        print(key)
        for value in values:
            print(value)


def base_buy_ticket(base, route_name):
    place = input('Введите желаемое место\n')
    place_key = f'Место №{place}'
    print(place_key)
    if place_key not in base:
        username_fio = f'Пассажир: {input("Введите фамилию и инициалы в формате: Фамилия И.О.\n")}'
        passport_details = f'Паспорт: {input("Укажите серию и номер паспорта в формате: XX XX XXXXXX\n")}'
        ticket_number = f'Билет №{random.randint(7593096766600, 7593096766700)}'
        base_append(
            base, place_key, ticket_number, route_name, username_fio, passport_details
        )  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
        base_print(base)  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
        return True
    else:
        print(f'{place_key} занято')
        return False


choice = input('Добро пожаловать, хотите приобрести билет? ').lower()
while True:
    if choice == 'да':
        route = input(
            'Доступные маршруты: Saint-Petersburg -> Pavlovsk [1], Saint-Petersburg -> Vyborg [2],\
 Saint-Petersburg -> Krondstadt[3], введите цифру желаемого маршрута\n'
        )
        base, route_name = id_route_mapping[int(route)]
        if base_buy_ticket(base, route_name):
            break
    else:
        print('До свидания!')
        break
