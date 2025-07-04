# Представьте, что вы храните ваши сбережения в бивалютном портфеле: 50% в рублях, а 50% в долларах.
# Один раз сбалансировав портфель по текущему курсу (количество долларов * курс == количество рублей),
# с изменением курса доллара, ваш портфель через какое-то время разбалансируется.
# Ваши сбережения в одной из валют станут стоить больше, чем в другой.
# Напишите программу, которая спрашивает у вас количество долларов с точностью до центов,
# количество рублей с точностью до копеек и какой сейчас курс доллара в рублях с точностью до копеек.
# Потом программа сообщает вам, сколько из ваших долларов надо обменять по курсу на рубли
# (или наоборот — сколько из ваших рублей обменять на доллары), чтобы портфель опять стал сбалансирован.
# Опять же, с точностью до копеек или центов.
# https://i.imgur.com/haSYAti.png


def dual_currency_count(exchange_rate, current_rubles, current_dollars):
    transfer_to_rubles = current_dollars * exchange_rate  # перевод из долларов в рубли
    average = (transfer_to_rubles + current_rubles) / 2
    diff = abs(average - current_rubles)
    if transfer_to_rubles > current_rubles:
        print(f'Вам надо продать доллары на {diff} рублей')
    elif transfer_to_rubles < current_rubles:
        print(f'Вам надо докупить доллары на {diff} рублей')
    else:
        print('Ваш портфель сбалансирован')


exchange_rate = float(input('Курс доллара:\n'))
current_rubles = float(input('Сколько у вас рублей?\n'))
current_dollars = float(input('Сколько у вас долларов?\n'))
dual_currency_count(exchange_rate, current_rubles, current_dollars)
