# 3)Написать класс конвертирования валют (USD, EUR, RUB)
# https://i.imgur.com/3NOJLi4.png

import requests

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
DOMAIN = os.getenv('DOMAIN')


class ConvertCurrency:
    def get_rates(self, from_currency: str, to_currency: str, count: int) -> float:
        response = requests.get(f'{DOMAIN}?access_key={TOKEN}')
        data = response.json()
        self.rates = data['rates']
        self.result_currency = (count * self.rates[from_currency]) / self.rates[to_currency]
        return self.result_currency


print(
    'Добро пожаловать в программу для перевода из одной валюты в другую!\n'
    'Вводите валюту в соответствии с кодом ISO 4217 (RUB, USD, EUR)',
)
converter = ConvertCurrency()
currency_from = input('Валюта из который переводите:\n').upper()
currency_to = input('Валюта в которую переводите:\n').upper()
count_to = int(input(f'Введите, сколько вы хотите {currency_to}\n'))
result = converter.get_rates(currency_from, currency_to, count_to)
print(f'Для покупки {count_to} {currency_to} вам небходимо потратить {result} {currency_from}')
