# Задание:
# Написать программу дневник:
# Спрашиваем у пользователя дату
# Просим написать сообщение ( запись в дневник )
# Создаём файл diary.txt

# В него записывается всё записи + дата в таком формате:
# 01.01.2020
# Привет, это первая запись

# Записи дополняются и корректно отображатся в файле со всеми отступами
# Условия: использовать функции и циклы
# В ответ прислать ссылку на гугл диск с файлами вашей программы

print('Welcome to L I S T !')
while True:
    choice = input('1. Сделать запись\n2. Закрыть дневник\n')
    if choice == '1':
        date = input('Введите дату в формате число.месяц.год - xx.xx.xxxx:\n')
        date += '\n'
        message = input('Запись в дневник:\n')
        message += '\n'
        date_message_array = {date: message}
        with open('diary.txt', 'a', encoding='utf-8') as file_diary:
            for date, message in date_message_array.items():
                file_diary.write(date)
                file_diary.write(message)
    elif choice == '2':
        break
    else:
        print('Ошибка, выберите, что сделать')
