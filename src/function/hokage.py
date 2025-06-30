# Задание для ниндзя на пути к званию хокаге (необязательно выполнять, но можете попробовать):

# Как вы знаете, в русском языке форма слова зависит от контекста.
# Один «крокодил», но два — «крокодила», а 10 — уже «крокодилов».
# Напишите метод, который на вход принимает число и три формы слова, а на выходе возвращает правильную форму слова
# для использования с этим числом.
# Предложите юзеру ввести число и выдайте ему любое количество крокодилов (или ежей, или любых других животных).
# https://i.imgur.com/9qxKBQD.png
def form_word(entered_honey_badger):
    honey_badger = 'медоед'
    if entered_honey_badger in range(11, 20):
        print(f'Вот вам {entered_honey_badger} {honey_badger + "ов"}')
    else:
        count_honey_badger = entered_honey_badger % 10
        form_medoed = [1]
        form_medoeda = [2, 3, 4]
        if count_honey_badger in form_medoed:
            print(f'Вот вам {entered_honey_badger} {honey_badger}')
        elif count_honey_badger in form_medoeda:
            print(f'Вот вам {entered_honey_badger} {honey_badger + "а"}')
        else:
            print(f'Вот вам {entered_honey_badger} {honey_badger + "ов"}')


entered_honey_badger = int(input('Сколько вам медоедов:\n'))
form_word(entered_honey_badger)
