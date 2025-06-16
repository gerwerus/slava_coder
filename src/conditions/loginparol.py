# Задание:ы
# Доработать программу с авторизацией и регистрацией.
# 1.1 При регистрации спрашивать у пользователя повторно ввести пароль, если пароли не совпадают, то вывести ошибку.
# https://i.imgur.com/nQaMdcl.png
# 1.2 Если пароль введён неверно, то вывести "Ошибка" при авторизации.
# https://i.imgur.com/F5JUHd3.png

print("Регистрация на сайте chicken.net")
login = input("Введите логин: ")
password = input("Введите пароль: ")
password_1 = input("Введите пароль повторно: ")
if password == password_1:
    print("Вы зарегистрировались!")
    print("Авторизация на сайте chiken.net")
    new_login = input("Введите логин: ")
    password_2 = input("Введите пароль: ")
    if new_login == login and password_2 == password:
        print("Вы успешно авторизовались!")
    else:
        print("Ошибка авторизации!")
else:
    print("Ошибка, пароль неверный!")
