# Доработать программу регистрации и авторизации в уроке:
# 3.1 Добавить функцию изменения пароля пользователя
# 3.2 При 3 неудачных попытках входа в систему прерывать работу программы
# 3.3 Если логин существует, то прервать регистрацию
# 3.4 При регистрации у каждого пользователя создаётся уникальный ID
# 3.5 Запрет на использование символа # в логине
import uuid


def password_change_func(password_last, password_last_confirm):
    if password_last == password_last_confirm and password_last == base[login]:
        print('Пароли совпадают')
        password_change = input('Введите новый пароль: ')
        password_change_confirm = input('Введите новый пароль повторно: ')
        if password_change == password_change_confirm:
            base[login] = password_change
            print('Вы успешно сменить пароль!')
            print(base)
    else:
        print('Пароли не совпадают')


base = {}
i = 0
print('Добро пожаловать в наше приложение!')
while True:
    choice = input(
        'Введите 1, чтобы зарегистрироваться \nВведите 2, чтобы авторизоваться\nВведите 3, чтобы выйти из программы\n'
    )
    print(base)
    if choice == '1':  # ПРОЦЕСС РЕГИСТРАЦИИ
        print('Процесс регистрации')

        login = input('Введите логин: \n')
        if not login.isalpha():
            print('Запрещено использовать символы')
            continue
        else:
            if login in base:
                print('Такой логин уже существует')
                continue
        password = input('Введите пароль: \n')
        if password == '':
            print('Пароль не может быть пустой строкой')
            continue

        password_confirm = input('Введите пароль повторно: \n')
        if password == password_confirm:
            user_uuid = uuid.uuid4()  # Создание случайного UUID
            base[login] = {'password': password_confirm, 'uuid': str(user_uuid)}  # ПРИСВОЕНИЕ ЛОГИНУ UUID И ПАРОЛЯ
            print(f'Вы успешно зарегистрировались! Ваш UUID: {user_uuid}')
        elif password != password_confirm:
            print('Пароли не совпадают!')
            continue
    elif choice == '2':  # ПРОЦЕСС АВТОРИЗАЦИИ
        while i < 3:
            print('Процесс авторизации')
            login = input('Введите логин: \n')
            if login in base:
                password = input('Введите пароль: \n')
                if password == base[login]:
                    print('Вы успешно вошли в систему')
                    print(base)
                    choice_password = input('Нажмите 1, чтобы сменить пароль \nНажмите 2, чтобы оставаться в системе\n')
                    if choice_password == '1':
                        password_last = input('Введите старый пароль: ')
                        password_last_confirm = input('Введите старый пароль повторно: ')
                        password_change_func(password_last, password_last_confirm)  # СМЕНА ПАРОЛЯ
                        break
                    elif choice_password == '2':
                        print('Вы в системе!')
                        break
                elif password != base[login]:  # 3 ПОПЫТКИ ВХОДА ПРИ НЕПРАВИЛЬНОМ ПАРОЛЕ
                    i += 1
                    print('Пароль не верный')

            else:
                print('Такой пользователь не зарегистрирован')
                continue
        else:
            print('Вы использовали все попытки, доступ авторизации недоступен')
            break
    elif choice == '3':  # ВЫХОД ИЗ СИСТЕМЫ
        print('Вы вышли из программы')
        break
