# Написать программу магазина с функциями:
# 3.1 Добавления товаров по разделу (смотреть урок практики) ✅
# 3.2 Удаление товаров из раздела без удаления самого раздела ✅
# 3.3 Вывод всех товаров и разделов ✅
# 3.4 Вывод всех товаров выбранного раздела ✅
# 3.5 Функция снижения и повышения цены на какой-либо товар ✅
# 3.6 Удаление раздела ✅


def product_price_change(shop):
    product_print(shop)
    print('Выберите что сделать: ')
    choice_change = input('1. Снизить\n2. Повысить\n')
    if choice_change == '1' or choice_change == '2':
        price_change = int(input('Сумма изменения:\n'))
        product_group = input('Выберите раздел\n')
        if product_group in shop:
            product = input('Выберите продукт\n')
            if product in shop[product_group]:
                for product, price in shop[product_group].items():
                    if choice_change == '1':
                        price_new = price - price_change
                        shop[product_group].update({product: price_new})
                    elif choice_change == '2':
                        price_new = price + price_change
                        shop[product_group].update({product: price_new})
                return shop
            else:
                print('Такого продукта не существует')
        else:
            print('Такого раздела не существует')
    else:
        print('Ошибка')


def product_print(shop):  # Печать товаров
    if choice == '3':  # Печать всех товаров
        for group, array in shop.items():
            print('Раздел: ' + group)
            for products, price in array.items():
                print(products + ' - ' + str(price))
    elif choice == '4':  # Печать товаров выбранного раздела
        print(f'Раздел: {choice_group}')
        for product, price in shop[choice_group].items():
            print(f'{product} - {price}')


def products_add(user_group, shop, product, cost, products):
    if user_group in shop:
        shop[user_group].update(products)
        print(f'Товар {product} добавлен c ценой {cost}')
    elif user_group not in shop:
        shop.update({user_group: {}})
        shop[user_group].update(products)
        print(f'Создан раздел {user_group} и добавлен товар {product} с ценой {cost}')
    else:
        return 'Ошибка'
    return shop


def products_del(shop):
    user_group = input('Выберите раздел:\n').lower()
    if user_group in shop:
        product = input('Какой продукт удалить?\n').lower()
        if product in shop[user_group]:
            del shop[user_group][product]
            print(f'Товар {product} удален')
            return shop
        else:
            print('Такой товар не найден!')
    else:
        print('Такой раздел не найден!')


def group_del(shop):
    user_group = input('Выберите раздел:\n').lower()
    if user_group in shop:
        del shop[user_group]
        print(f'Раздел {user_group} удален')
        return shop
    else:
        print('Такой раздел не найден')


shop = {'мучное': {'хлеб': 50, 'пряники': 70}, 'молочное': {'молоко': 100}}


print('Вы находитесь в меню редактирования!')
while True:
    choice = input(
        '1. Добавить товар в раздел\n2. Удалить товар из раздела\n3. Вывести все товары и разделы\n'
        '4. Вывести товары выбранного раздела\n5. Повысить/Снизить цену товаров\n6. Удалить раздел\n'
        '7. Выйти из программы\n'
    )
    if choice == '1':
        user_group = input('Выберите раздел:\n').lower()
        product = input('Какой продукт добавить?\n').lower()
        if product not in shop[user_group]:
            cost = int(input('Укажите цену\n'))
            products_add(user_group, shop, {product: cost})
        else:
            print(f'{product} уже есть в магазине')
    elif choice == '2':
        products_del(shop)
    elif choice == '3':
        product_print(shop)
    elif choice == '4':
        choice_group = input('Введите раздел\n').lower()
        product_print(shop)
    elif choice == '5':
        choice = '3'
        product_price_change(shop)
    elif choice == '6':
        group_del(shop)
    elif choice == '7':
        print('Выход из программы!')
        break
