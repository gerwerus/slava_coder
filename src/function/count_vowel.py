# Напишите функцию, которая считает количество гласных в переданной строке.
# Программа должна спросить у пользователя в консоли слово и вывести количество гласных в нем.
# Пример:
# https://i.imgur.com/8XxoOL8.png
def count_vowel(word_input):
    word_list = list(word_input)
    vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    consonant = [
        'б',
        'в',
        'г',
        'д',
        'ж',
        'з',
        'й',
        'к',
        'л',
        'м',
        'н',
        'п',
        'р',
        'с',
        'т',
        'ф',
        'х',
        'ц',
        'ч',
        'ш',
        'щ',
    ]
    vowel_in_word = []
    consonant_in_word = []
    for i in word_list:
        if i in vowel:
            vowel_in_word.append(i)
        elif i in consonant:
            consonant_in_word.append(i)
        else:
            continue
    vewel_count = len(vowel_in_word)
    consonant_count = len(consonant_in_word)
    print(f'Гласных {vewel_count}')
    print(f'Согласных {consonant_count}')


word_input = input('Введите слово:\n')
count_vowel(word_input)
