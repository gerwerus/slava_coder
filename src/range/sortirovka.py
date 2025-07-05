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
def sort_group_age(entered_age):
    if entered_age in range(0, 12):
        return 'дети'
    elif entered_age in range(12, 18):
        return 'подростки'
    elif entered_age in range(18, 27):
        return 'клуб 27'
    elif entered_age in range(27, 45):
        return 'молодые'
    elif entered_age in range(45, 60):
        return 'зрелые'
    elif entered_age in range(60, 74):
        return 'пожилые'
    elif entered_age in range(74, 90):
        return 'молодые в душе'
    else:
        return 'долгожители'


entered_age = int(input('Введите ваш возраст:\n'))
print(f'Вы занесены в группу - {sort_group_age(entered_age)}')
