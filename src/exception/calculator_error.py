# Написать функцию деления одного числа на другое:
# Если пользователь пытается делить число на ноль, то обрабатываем ошибку и выводим -
# "На ноль делить нельзя" и запускаем программу заново.
# https://i.imgur.com/xDXG7Ph.png
print('Программа деления на ноль')
loop = True
entered_number_one = int(input('Введите число 1:\n'))
while loop:
    entered_number_two = int(input('Введите число 2:\n'))
    try:
        result = entered_number_one / entered_number_two
        loop = False
    except ZeroDivisionError:
        print('На ноль делить нельзя')

print(f'Вы получили ответ: {result}')
