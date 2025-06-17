# Напишите программу, которая перевернет порядок элементов любого исходного массива. Переверните массив сами с помощью цикла. https://i.imgur.com/A5EW7bD.png
# Пробовал так
n = int(input('Введите число n: '))
b = list(range(n))

for i in reversed(b):
    print(i)
# Сделал сначала с перевернутым массивом, Потом пытался долго понять как это сделать без перевернутого и пришел к такому
number = int(input('Введите число n: '))
a = list(range(number))
result = []
for j in a[::-1]:
    result.append(j)
print(result)
