# 1.) Напишите функцию, которая принимает на вход имя и отчество, а выводит инициалы (первые буквы с точками без пробела
# между ними).
# https://i.imgur.com/tBGNfwr.png


def print_fio(user_name, user_patronymic):
    return f'{user_name[0]}.{user_patronymic[0]}.'


user_surname = input('Введите фамилию:\n')
user_name = input('Введите имя:\n')
user_patronymic = input('Введите отчество:\n')

print(f'{user_surname} {print_fio(user_name, user_patronymic)}')
