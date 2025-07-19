# Кредитная заявка. Написать программу, которая оценивает, выдавать ли кредит по кредитной заявке.
# Программа спрашивает у пользователя ФИО, возраст, пол, доход в месяц, наличие кредитной истории и запрашиваемая сумма.
# Если возраст от 21 до 40 — +10 баллов
# Если возраст больше 40 — +20 баллов
# Если заявитель — женщина — +10 баллов
# Если доход заявителя от 20 000 до 40 000 — +10 баллов
# Если доход заявителя от 40 000 — + 20 баллов
# Если у заявителя есть кредитная история — +20 баллов
# Если запрашиваемая сумма меньше 20 000 рублей — +20 баллов
# Если запрашиваемая сумма от 20 000 до 40 000 — +10 баллов
# Если балл больше либо равен 50, то выдать, иначе - отказать.
# Также выведите информацию о том, сколько клиенту банка платить в месяц с учётом процентов (5%).
from dataclasses import dataclass
from enum import StrEnum

AGE_MIN = 21
AGE_MAX = 40
INCOME_MIN = 20000
INCOME_MAX = 40000
REQUESTED_AMOUNT_MIN = 20000
REQUESTED_AMOUNT_MAX = 40000
BONUS_MIN = 10
BONUS_MAX = 20
CREDIT_SCORE = 50
CREDIT_PROCENT = 5


class Gender(StrEnum):
    MALE = 'мужской'
    FEMALE = 'женский'


@dataclass
class EstimationCredit:
    fio: str
    age: int
    gender: Gender
    monthly_income: float
    credit_history: str
    requested_amount: float
    payment_month: int

    def get_consent(self) -> bool:
        score = 0
        if age >= AGE_MIN and age <= AGE_MAX:
            score += BONUS_MIN
        elif age > AGE_MAX:
            score += BONUS_MAX
        if gender == Gender.FEMALE:
            score += BONUS_MIN
        if monthly_income >= INCOME_MIN and monthly_income <= INCOME_MAX:
            score += BONUS_MIN
        elif monthly_income > INCOME_MAX:
            score += BONUS_MAX
        if credit_history == 'да':
            score += BONUS_MAX
        if requested_amount < REQUESTED_AMOUNT_MIN:
            score += BONUS_MAX
        elif requested_amount >= REQUESTED_AMOUNT_MIN and requested_amount >= REQUESTED_AMOUNT_MAX:
            score += BONUS_MIN
        return score >= CREDIT_SCORE

    def get_monthly_percentage_payment(self) -> float:
        result_month_payment = requested_amount / payment_month
        result_month_procent = (result_month_payment * CREDIT_PROCENT) / 100
        return result_month_payment + result_month_procent


fio = input('Введите ФИО: ')
age = int(input('Введите возраст: '))
gender = input('Введите пол (мужской/женский): ')
monthly_income = float(input('Введите ваш ежемесячный доход: '))
credit_history = input('У вас есть кредитная история (да/нет): ')
requested_amount = float(input('Какую сумму вы расчитываете получить: '))
payment_month = int(input('За сколько месяцев вы сможете выплатить кредит: '))
estimation_credit = EstimationCredit(fio, age, gender, monthly_income, credit_history, requested_amount, payment_month)
credit_consent = estimation_credit.get_consent()
result_payment_month = estimation_credit.get_monthly_percentage_payment()
if credit_consent:
    print(
        f'{fio} вам одобрен кредит в размере {requested_amount} с ежемесячной выплатой {result_payment_month}'
        f' с учетом ставки {CREDIT_PROCENT}%',
    )
else:
    print(f'{fio}, извините, вам отказано!')
