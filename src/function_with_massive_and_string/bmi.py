# 3)Индекс массы тела (англ. body mass index (BMI), ИМТ) — величина, позволяющая оценить
# степень соответствия массы человека и его роста и тем самым косвенно оценить, является ли масса недостаточной,
# нормальной или избыточной.
# Вычисляется этот индекс по простой формуле — масса в килограммах, деленная на квадрат роста в метрах.
# Программа должна спрашивать у пользователя его параметры, вычислять его индекс массы тела,
# а потом выдавать вердикт по таблице из Википедии.
# https://i.imgur.com/NHbQvqr.png


import pandas as pd


def print_result_bmi(bmi: float) -> str:
    if bmi <= int(16):
        bmi_determination = 'Выраженный дефицит массы телы'
    elif bmi <= int(18.5):
        bmi_determination = 'Недостаточная (дефицит) масса тела'
    elif bmi <= int(25):
        bmi_determination = 'Норма'
    elif bmi <= int(30):
        bmi_determination = 'Избыточная масса тела (предожирение)'
    elif bmi <= int(35):
        bmi_determination = 'Ожирение 1 степени'
    elif bmi <= int(40):
        bmi_determination = 'Ожирение 2 степени'
    elif bmi > int(40):
        bmi_determination = 'Ожирение 3 степени'
    return bmi_determination


tables = pd.read_html(
    'https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D0%BC%D0%B0%D1%81%D1%81%D1%8B_'
    '%D1%82%D0%B5%D0%BB%D0%B0')
print(tables[0])
weight = float(input('Введите ваш вес (кг):\n'))
height = float(input('Введите ваш рост (м):\n'))
bmi = weight / height**2
print(f'Ваш индекс: {bmi}')
print(f'Ваша категория: {print_result_bmi(bmi)}')
