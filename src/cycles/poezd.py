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


def base_append_pavlovsk():
    base_details = []
    base_details.append(ticket_number)
    base_details.append(route_name)
    base_details.append(username_fio)
    base_details.append(pasport_details)
    base_pavlovsk[place_key] = base_details


def base_append_vyborg():
    base_details = []
    base_details.append(ticket_number)
    base_details.append(route_name)
    base_details.append(username_fio)
    base_details.append(pasport_details)
    base_vyborg[place_key] = base_details


def base_append_kronstadt():
    base_details = []
    base_details.append(ticket_number)
    base_details.append(route_name)
    base_details.append(username_fio)
    base_details.append(pasport_details)
    base_kronstadt[place_key] = base_details


def base_print_pavlosk():
    for key, values in base_pavlovsk.items():
        print(key)
        for value in values:
            print(value)


def base_print_vyborg():
    for key, values in base_vyborg.items():
        print(key)
        for value in values:
            print(value)


def base_print_kronstadt():
    for key, values in base_kronstadt.items():
        print(key)
        for value in values:
            print(value)


base_pavlovsk = {
    'Место №1': [
        'Билет №7593096766601',
        'Маршрут: Saint-Petersburg -> Pavlovsk',
        'Пассажир: Петров Н.Е.',
        'Паспорт: 23 23 434343',
    ],
    'Место №2': [
        'Билет №7593096766602',
        'Маршрут: Saint-Petersburg -> Pavlovsk',
        'Пассажир: Куличев Н.Е.',
        'Паспорт: 24 24 444444',
    ],
    'Место №3': [
        'Билет №7593096766603',
        'Маршрут: Saint-Petersburg -> Pavlovsk',
        'Пассажир: Улуханов Н.Е.',
        'Паспорт: 25 25 454545',
    ],
}
base_vyborg = {
    'Место №1': [
        'Билет №7593096766601',
        'Маршрут: Saint-Petersburg -> Vyborg',
        'Пассажир: Петров Н.Е.',
        'Паспорт: 23 23 434343',
    ],
    'Место №2': [
        'Билет №7593096766602',
        'Маршрут: Saint-Petersburg -> Vyborg',
        'Пассажир: Куличев Н.Е.',
        'Паспорт: 24 24 444444',
    ],
    'Место №3': [
        'Билет №7593096766603',
        'Маршрут: Saint-Petersburg -> Vyborg',
        'Пассажир: Улуханов Н.Е.',
        'Паспорт: 25 25 454545',
    ],
}
base_kronstadt = {
    'Место №1': [
        'Билет №7593096766601',
        'Маршрут: Saint-Petersburg -> Kronstadt',
        'Пассажир: Петров Н.Е.',
        'Паспорт: 23 23 434343',
    ],
    'Место №2': [
        'Билет №7593096766602',
        'Маршрут: Saint-Petersburg -> Kronstadt',
        'Пассажир: Куличев Н.Е.',
        'Паспорт: 24 24 444444',
    ],
    'Место №3': [
        'Билет №7593096766603',
        'Маршрут: Saint-Petersburg -> Kronstadt',
        'Пассажир: Улуханов Н.Е.',
        'Паспорт: 25 25 454545',
    ],
}
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
                base_append_pavlovsk()  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
                base_print_pavlosk()  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
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
                base_append_vyborg()  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
                base_print_vyborg()  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
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
                base_append_kronstadt()  # СОЗДАНИЕ МАССИВА С ДАННЫМИ, И ЕГО ДОБАВЛЕНИЕ В БАЗУ ВЫБРАННОГО МАРШРУТА
                base_print_kronstadt()  # ВЫВОД В СТОЛБИК ДАННЫХ О БИЛЕТЕ
                break
    else:
        print('До свидания!')
        break
