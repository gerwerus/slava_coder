# 1)Пользователь делает вклад в размере N рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающую аргументы N и years, и возвращающую сумму, которая будет на счету пользователя.
# https://i.imgur.com/Xxx5T7e.png

BANK_PROCENT = 10


def bank_invest_counting(invest_money: int, invest_years: int) -> float:  # Подсчет вклада пользователя
    years = 0
    while years < invest_years:
        years += 1
        capital_profit = (BANK_PROCENT * invest_money) / 100
        invest_money += capital_profit
    return invest_money


invest_money = int(input('Сколько у вас денег?\n'))
invest_years = int(input('На сколько лет хотите сделать вклад?\n'))
print(f'По итогу вы получите {bank_invest_counting(invest_money, invest_years)}')
