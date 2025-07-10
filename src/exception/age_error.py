# Напишите программу, которая выводит возраст человека. Если введено не число, то программа об этом указывает.
# https://i.imgur.com/i5jCaws.png
loop = True
while loop:
    try:
        age = int(input('Введите ваш возраст:\n'))
        loop = False
    except ValueError:
        print('Введите число')
print(f'Вам {age} лет')
