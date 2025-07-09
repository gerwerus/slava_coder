# 3)Индекс массы тела (англ. body mass index (BMI), ИМТ) — величина, позволяющая оценить
# степень соответствия массы человека и его роста и тем самым косвенно оценить, является ли масса недостаточной,
# нормальной или избыточной.
# Вычисляется этот индекс по простой формуле — масса в килограммах, деленная на квадрат роста в метрах.
# Программа должна спрашивать у пользователя его параметры, вычислять его индекс массы тела,
# а потом выдавать вердикт по таблице из Википедии.
# https://i.imgur.com/NHbQvqr.png
# >>> from enum import Enum

# >>> class Day(Enum):
# ...     MONDAY = 1
# ...     TUESDAY = 2
# ...     WEDNESDAY = 3
# ...     THURSDAY = 4
# ...     FRIDAY = 5
# ...     SATURDAY = 6
# ...     SUNDAY = 7
# ...

# >>> list(Day)
# [
#     <Day.MONDAY: 1>,
#     <Day.TUESDAY: 2>,
#     <Day.WEDNESDAY: 3>,
#     <Day.THURSDAY: 4>,
#     <Day.FRIDAY: 5>,
#     <Day.SATURDAY: 6>,
#     <Day.SUNDAY: 7>
# ]

from enum import IntEnum
import pandas as pd


class WeightIndex(IntEnum):
    VERY_LOW = 16
    LOW = 18.5
    NORMAL = 25
    HIGH = 30
    HIGH_1 = 35
    HIGH_2 = 40
    HIGH_3 = 40


def print_result_bmi(bmi: float) -> str:
    if bmi <= WeightIndex.VERY_LOW:
        bmi_determination = 'Выраженный дефицит массы телы'
    elif bmi <= WeightIndex.LOW:
        bmi_determination = 'Недостаточная (дефицит) масса тела'
    elif bmi <= WeightIndex.NORMAL:
        bmi_determination = 'Норма'
    elif bmi <= WeightIndex.HIGH:
        bmi_determination = 'Избыточная масса тела (предожирение)'
    elif bmi <= WeightIndex.HIGH_1:
        bmi_determination = 'Ожирение 1 степени'
    elif bmi <= WeightIndex.HIGH_2:
        bmi_determination = 'Ожирение 2 степени'
    elif bmi > WeightIndex.HIGH_3:
        bmi_determination = 'Ожирение 3 степени'
    return bmi_determination


tables = pd.read_html(
    'https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D0%BC%D0%B0%D1%81%D1%81%D1%8B_'
    '%D1%82%D0%B5%D0%BB%D0%B0',
)
print(tables[0])
weight = float(input('Введите ваш вес (кг):\n'))
height = float(input('Введите ваш рост (м):\n'))
bmi = weight / height**2
print(f'Ваш индекс: {bmi}')
print(f'Ваша категория: {print_result_bmi(bmi)}')
