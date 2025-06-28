# Напишите функцию, которая определяет является ли слово палиндромом https://i.imgur.com/LJrALR5.png
def found_palindrom(word_input):
    word_flip = word_input[::-1]
    if word_input == word_flip:
        print(f'Слово {word_input} - это палиндром')
    else:
        print(f'Слово {word_input} - это не палиндром')


word_input = input('Введите слово:\n')
found_palindrom(word_input)
