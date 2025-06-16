# Сделать собственную программу для оценивания.

# Если оценка от 4.5 до 5, то программа выводит отлично (5 звёзд)
# Если от 3.5 до 4.5, то программа выводит хорошо (4 звезды)
# Если от 2.5 до 3.5, то программа выводит нормально (3 звезды)
# Если от 1.5 до 2.5, то программа выводит плохо (2 звезды)
# Если от 0 до 1.5, то программа выводит ужасно (1 звезда)
# Оценивать в звездах ⭐

import emoji
print('Пожалуйста, оцените обслуживание в отеле!')
grade = float(input('Введите оценку: '))

star_code = ':star:'
star_emoji = emoji.emojize(star_code)
stars_5 = f'{star_emoji} ' * 5
stars_4 = f'{star_emoji} ' * 4
stars_3 = f'{star_emoji} ' * 3
stars_2 = f'{star_emoji} ' * 2
stars_1 = f'{star_emoji} ' * 1
if grade >= 4.5 and grade <= 5:
    print('Отлично', stars_5)
elif grade >= 3.5 and grade < 4.5:
    print('Хорошо', stars_4)
elif grade >= 2.5 and grade < 3.5:
    print('Нормально', stars_3)
elif grade >= 1.5 and grade < 2.5:
    print('Плохо', stars_2)
elif grade >= 0 and grade < 1.5:
    print('Ужасно', stars_1)
