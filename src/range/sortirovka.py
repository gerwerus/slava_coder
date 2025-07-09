# Написать программу "Сортировка людей по возрасту".
# От 0 до 12 - дети
# От 12 до 18 - подростки
# От 18 до 27 - клуб 27
# От 27 до 45 - молодые
# От 45 до 60 - зрелые
# От 60 до 74 - пожилые
# От 74 до 90 - молоды в душе
# От 90 и выше - долгожители
# Вы занесены в группу - взрослые
# МБ какую-нибудь валидацию прикрутить? (Если пользователь ввел -2, а если 350?) 130
MINIMUM_AGE = 0
MAXIMUM_AGE = 130


def sort_group_age(entered_age: int) -> str:
    if entered_age in range(0, 12):
        people_group = 'дети'
    elif entered_age in range(12, 18):
        people_group = 'подростки'
    elif entered_age in range(18, 27):
        people_group = 'клуб 27'
    elif entered_age in range(27, 45):
        people_group = 'молодые'
    elif entered_age in range(45, 60):
        people_group = 'зрелые'
    elif entered_age in range(60, 74):
        people_group = 'пожилые'
    elif entered_age in range(74, 90):
        people_group = 'молодые в душе'
    else:
        people_group = 'долгожители'
    return people_group


entered_age = int(input('Введите ваш возраст:\n'))
if entered_age < MINIMUM_AGE or entered_age > MAXIMUM_AGE:
    print('Проверьте правильность ввода возраста!')
else:
    print(f'Вы занесены в группу - {sort_group_age(entered_age)}')
