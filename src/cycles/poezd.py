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

from const.poezd_const import base_pavlovsk, base_vyborg, base_kronstadt

import random


def base_append(base, base_pavlovsk, base_vyborg, base_kronstadt):
    base['Билеты в Павлоск'] = base_pavlovsk
    base['Билеты в Выборг'] = base_vyborg
    base['Билеты в Крондштат'] = base_kronstadt


def base_print(base):
    for key, value in base.items():
        print(key)
        for key2, value2 in value.items():
            print(key2)
            for value3 in value2:
                print(value3)


base = {}


choice = input('Добро пожаловать, хотите приобрести билет? ').lower()
while True:
    if choice == 'да':
        route = input(
            'Доступные маршруты: Saint-Petersburg -> Pavlovsk [1], Saint-Petersburg -> Vyborg [2],\
 Saint-Petersburg -> Krondstadt[3], введите цифру желаемого маршрута\n'
        )
        if route == '1':
            route_name = 'Маршрут: Saint-Petersburg -> Pavlovsk'
            place = input('Введите желаемое место\n')
            place_key = f'Место №{place}'
            print(place_key)
            if place_key not in base_pavlovsk:
                username_fio = f'Пассажир: {input("Введите фамилию и инициалы в формате: Фамилия И.О.\n")}'
                pasport_details = f'Паспорт: {input("Укажите серию и номер паспорта в формате: XX XX XXXXXX\n")}'
                ticket_number = f'Билет №{random.randint(7593096766600, 7593096766700)}'
                base_pavlovsk[place_key] = [ticket_number, route_name, username_fio, pasport_details]
                base_append(
                    base, base_pavlovsk, base_vyborg, base_kronstadt
                )  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
                base_print(base)  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
                break
            else:
                print(f'{place_key} занято')

        elif route == '2':
            route_name = 'Маршрут: Saint-Petersburg -> Vyborg'
            place = input('Введите желаемое место\n')
            place_key = f'Место №{place}'
            print(place_key)
            if place_key not in base_vyborg:
                username_fio = f'Пассажир: {input("Введите фамилию и инициалы в формате: Фамилия И.О.\n")}'
                pasport_details = f'Паспорт: {input("Укажите серию и номер паспорта в формате: XX XX XXXXXX\n")}'
                ticket_number = f'Билет №{random.randint(7593096766600, 7593096766700)}'
                base_vyborg[place_key] = [ticket_number, route_name, username_fio, pasport_details]
                base_append(
                    base, base_pavlovsk, base_vyborg, base_kronstadt
                )  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
                base_print(base)  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
                break

            else:
                print(f'{place_key} занято')

        elif route == '3':
            route_name = 'Маршрут: Saint-Petersburg -> Krondstat'
            place = input('Введите желаемое место\n')
            place_key = f'Место №{place}'
            print(place_key)
            if place_key not in base_kronstadt:
                username_fio = f'Пассажир: {input("Введите фамилию и инициалы в формате: Фамилия И.О.\n")}'
                pasport_details = f'Паспорт: {input("Укажите серию и номер паспорта в формате: XX XX XXXXXX\n")}'
                ticket_number = f'Билет №{random.randint(7593096766600, 7593096766700)}'
                base_kronstadt[place_key] = [ticket_number, route_name, username_fio, pasport_details]
                base_append(
                    base, base_pavlovsk, base_vyborg, base_kronstadt
                )  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
                base_print(base)  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
                break
            else:
                print(f'{place_key} занято')
    else:
        print('До свидания!')
        break
