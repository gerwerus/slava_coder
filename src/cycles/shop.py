def product_delete_func(product_delete):
    for i in shop:
        if str(i[0]) == product_delete:
            shop.remove(i)


def product_add_func(product_add):
    product_found = any(str(i[0]) == product_add for i in shop)
    if not product_found:
        product_m = [product_add, product_cost]
        shop.append(product_m)
        print(f'Товар {product_add} добавлен')
    else:
        print('Товар уже имеется в магазине')


def shop_print_func():
    for product_array in shop:
        print(product_array[0], '-', product_array[1], ' р.')


money = 500
bag = []

shop = [['котлеты', 100], ['гречка', 234], ['хлеб', 54]]

print('Добро пожаловать в наш магазин!')
username = input('Введите ваше имя: ')

if username.lower() == 'admin':  # КОД ДЛЯ АДМИНИСТРАТОРА
    print(f'В магазине сейчас имеются товары такие как: {shop}')
    while True:
        choice_adm = input('Выберите, удалить/добавить товар или выйти из системы: ').lower()
        if choice_adm == 'удалить':
            product_delete = input('Введите название товара, который хотите удалить: ').lower()
            product_delete_func(product_delete)  # УДАЛЕНИЕ ТОВАРА
            print(f'Товар {product_delete} удален')
        elif choice_adm == 'добавить':
            product_add = input('Введите название товара, который хотите добавить: ').lower()
            product_cost = int(input('Введите цену товара: '))
            product_add_func(product_add)  # ДОБАВЛЕНИЕ ТОВАРА
        elif choice_adm == 'выйти':
            print('Вы вышли из системы!')
            break
        print('Обновленный список товаров: ', shop)
elif username.lower() != 'admin':  # КОД ДЛЯ ПОКУПАТЕЛЯ
    while True:
        print('Выберите способ покупки:\n', '1. На месте\n', '2. Доставка\n', '3. Выход')
        choice = input()
        if choice.lower() == '1':  # ПОКУПКА НА МЕСТЕ
            print('В магазине имеются товар: ')
            shop_print_func()  # ПЕЧАТЬ ТОВАРОВ
            print('Сейчас у вас ', money, ' рублей')
            print('В сумке сейчас находятся: ')
            for i in bag:  # ПРОВЕРКА ДЕНЕГ
                print(i)
            if money <= 54:
                print('У вас недостаточно средств для покупок!')
                break
            product_choice = input('Что будете приобретать? ')
            found = False
            for product_array in shop:  # ПОКУПКА ТОВАРА
                if product_choice == product_array[0] and money >= product_array[1]:
                    money -= product_array[1]
                    bag.append(product_array[0])
                    print('С счёта списано ', product_array[1], ' рублей и ', product_array[0], ' добавлено в сумку')
                    found = True
            if not found:
                print('Такой товар не найден:')
        elif choice.lower() == '2':  # ДОСТАВКА
            shop_print_func()  # ПЕЧАТЬ ТОВАРОВ
            product_choice = input('Что будете приобретать?')
            for product_array in shop:  # ПОКУПКА ТОВАРА
                if product_choice == product_array[0]:
                    transfer.append(product_array[0])
                    print(f'Вы выбрали {product_choice}. Введите адресс доставки')
                    address = input()
                    print(
                        ' Ваш заказ:\n',
                        f'Имя - {username}\n',
                        f'Товар - {product_choice}\n',
                        f'Адресс доставки - {address}',
                    )
                    found = True
            if not found:
                print('Такой товар не найден:')
        else:
            print('Выход из магазина')
            break
