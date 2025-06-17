# Доработать программу для магазина. Также добавить админа - который может удалять, добавлять товары.
# Если не админ - то переходить к покупки
money = 500
bag = []

shop = [['котлеты', 100], ['гречка', 234], ['хлеб', 54]]

print('Добро пожаловать в наш магазин!')
username = input('Введите ваше имя: ')

if username.lower() == 'admin':
    print('Вы авторизовались как администратор!')
    print('В магазине сейчас лежат такие товары как: ', shop)
    edit = input('Редактировать товар?').lower()
    while edit == 'да':
        choice_adm = input('Выберите удалить или добавить товар: ')
        if choice_adm.lower() == 'удалить':
            product_delete = input('Введите название товара, который хотите удалить: ').lower()

            for i in shop:
                if i[0] == product_delete:
                    shop.remove(i)

            print(f'Товар {product_delete} удален')

        elif choice_adm.lower() == 'добавить':
            product_add = input('Введите название товара, который хотите добавить: ').lower()
            product_cost = int(input('Введите цену товара: '))

            if shop[0] != product_add:
                product_m = [product_add, product_cost]
                shop.append(product_m)
        print('Обновленный список товаров: ', shop)

else:
    choice = input('Будете что-то приобретать? ')
    while choice.lower() == 'да':
        print('В магазине имеются товар: ')
        for array in shop:
            print(array[0], '-', array[1], ' р.')

        print('Сейчас у вас ', money, ' рублей')
        print('В сумке сейчас находятся: ')
        for i in bag:
            print(i)
        if money <= 54:
            print('У вас недостаточно средств для покупок!')
            break
        choice_2 = input('Что будете преобретать? ')
        found = False
        for array in shop:
            if choice_2 in array[0] and money >= array[1]:
                money -= array[1]
                bag.append(array[0])
                print('С вашего счёта списано ', array[1], ' рублей и ', array[0], ' добавлено в сумку')
                found = True

        if not found:
            print('Такой товар не найден')

    else:
        print('Выход из магазина')
