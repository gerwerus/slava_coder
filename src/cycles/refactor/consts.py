pavlovsk_route_name = 'Saint-Petersburg -> Pavlovsk'
vyborg_route_name = 'Saint-Petersburg -> Vyborg'
kronstadt_route_name = 'Saint-Petersburg -> Kronstadt'


base_pavlovsk = {
    'Место №1': [
        'Билет №7593096766601',
        pavlovsk_route_name,
        'Пассажир: Петров Н.Е.',
        'Паспорт: 23 23 434343',
    ],
    'Место №2': [
        'Билет №7593096766602',
        pavlovsk_route_name,
        'Пассажир: Куличев Н.Е.',
        'Паспорт: 24 24 444444',
    ],
    'Место №3': [
        'Билет №7593096766603',
        pavlovsk_route_name,
        'Пассажир: Улуханов Н.Е.',
        'Паспорт: 25 25 454545',
    ],
}
base_vyborg = {
    'Место №1': [
        'Билет №7593096766601',
        vyborg_route_name,
        'Пассажир: Петров Н.Е.',
        'Паспорт: 23 23 434343',
    ],
    'Место №2': [
        'Билет №7593096766602',
        vyborg_route_name,
        'Пассажир: Куличев Н.Е.',
        'Паспорт: 24 24 444444',
    ],
    'Место №3': [
        'Билет №7593096766603',
        vyborg_route_name,
        'Пассажир: Улуханов Н.Е.',
        'Паспорт: 25 25 454545',
    ],
}
base_kronstadt = {
    'Место №1': [
        'Билет №7593096766601',
        kronstadt_route_name,
        'Пассажир: Петров Н.Е.',
        'Паспорт: 23 23 434343',
    ],
    'Место №2': [
        'Билет №7593096766602',
        kronstadt_route_name,
        'Пассажир: Куличев Н.Е.',
        'Паспорт: 24 24 444444',
    ],
    'Место №3': [
        'Билет №7593096766603',
        kronstadt_route_name,
        'Пассажир: Улуханов Н.Е.',
        'Паспорт: 25 25 454545',
    ],
}

id_route_mapping = {
    1: [base_pavlovsk, pavlovsk_route_name],
    2: [base_vyborg, vyborg_route_name],
    3: [base_kronstadt, kronstadt_route_name]
}
