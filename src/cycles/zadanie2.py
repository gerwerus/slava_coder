# Написать программу, которая выводит массив чисел от 1 до N. И выводит сумму всех чисел этого массива.
# Число N спрашивается у пользователя из консоли. https://i.imgur.com/yr6J6xv.
number = int(input('Введите число n: '))
massive = list(range(1,number + 1))
print(massive)
sum = sum(massive)
print(f'Сумма чисел: {sum}')
