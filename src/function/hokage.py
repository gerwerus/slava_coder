# Задание для ниндзя на пути к званию хокаге (необязательно выполнять, но можете попробовать):

# Как вы знаете, в русском языке форма слова зависит от контекста.
# Один «крокодил», но два — «крокодила», а 10 — уже «крокодилов».
# Напишите метод, который на вход принимает число и три формы слова, а на выходе возвращает правильную форму слова
# для использования с этим числом.
# Предложите юзеру ввести число и выдайте ему любое количество крокодилов (или ежей, или любых других животных).
# https://i.imgur.com/9qxKBQD.png
def honey_badger_word_form(entered_honey_badger):
    honey_badger = 'медоед'
    count_honey_badger_10 = entered_honey_badger % 10
    count_honey_badger_100 = entered_honey_badger % 100
    if count_honey_badger_100 in range(11, 20):
        return f'{honey_badger}ов'
    else:
        if count_honey_badger_10 == 1:
            return honey_badger
        elif count_honey_badger_10 in range(2, 5):
            return f'{honey_badger}а'
        else:
            return f'{honey_badger}ов'


entered_honey_badger = int(input('Сколько вам медоедов:\n'))
print(f'Вот вам {entered_honey_badger} {honey_badger_word_form(entered_honey_badger)}')

