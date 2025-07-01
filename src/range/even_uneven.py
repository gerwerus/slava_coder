# Задание:

# 1)Написать программу сортировки чисел:
# cгенерировать с помощью range массив из 300 чисел и отсортировать данный массив на чётные и нечётные числа
# по разным массивам, чтобы в одном хранились только чётные числа, а в другом только нечётные.

array = list(range(301))
even_array = []
uneven_array = []
for number in array:
    if number % 2 == 0:
        even_array.append(number)
    else:
        uneven_array.append(number)

print(f'Четные числа:\n{even_array}\nНечетные числа:\n{uneven_array}')
