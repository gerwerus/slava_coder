# Написать программу магазина с функциями:
# 3.1 Добавления товаров по разделу (смотреть урок практики) ✅
# 3.2 Удаление товаров из раздела без удаления самого раздела ✅
# 3.3 Вывод всех товаров и разделов ✅
# 3.4 Вывод всех товаров выбранного раздела ✅
# 3.5 Функция снижения и повышения цены на какой-либо товар ✅
# 3.6 Удаление раздела ✅


def change_price_product(shop):
    print_all_product(shop)
    print('Выберите что сделать: ')
    choice_change = input('1. Снизить\n2. Повысить\n')
    if choice_change not in ['1', '2']:
        print('Ошибка')
        return
    price_change = int(input('Сумма изменения:\n'))
    product_group = input('Выберите раздел\n')
    if product_group not in shop:
        print('Такого раздела не существует')
        return
    product = input('Выберите продукт\n')
    if product in shop[product_group]:
        if choice_change == '1':
            price_new = shop[product_group][product] - price_change
        elif choice_change == '2':
            price_new = shop[product_group][product] + price_change
        shop[product_group].update({product: price_new})
        return
    print('Такого продукта не существует')


def print_all_product(shop):
    for group, array in shop.items():
        print('Раздел: ' + group)
        for products, price in array.items():
            print(products + ' - ' + str(price))


def print_group_product(shop, choice_group):
    for product, price in shop[choice_group].items():
        print(f'{product} - {price}')


def add_products(entered_group, shop, products):
    if entered_group in shop:
        shop[entered_group].update(products)
        print(f'Товар {product} добавлен c ценой {cost}')
    elif entered_group not in shop:
        shop.update({entered_group: {products}})
        print(f'Создан раздел {entered_group} и добавлен товар {product} с ценой {cost}')
    else:
        return 'Ошибка'
    return


def del_products(shop):
    entered_group = input('Выберите раздел:\n').lower()
    if entered_group in shop:
        product = input('Какой продукт удалить?\n').lower()
        if product in shop[entered_group]:
            del shop[entered_group][product]
            print(f'Товар {product} удален')
            return
        print('Такой товар не найден!')
    else:
        print('Такой раздел не найден!')


def group_del(shop):
    entered_group = input('Выберите раздел:\n').lower()
    if entered_group in shop:
        del shop[entered_group]
        print(f'Раздел {entered_group} удален')
        return
    else:
        print('Такой раздел не найден')


shop = {'мучное': {'хлеб': 50, 'пряники': 70}, 'молочное': {'молоко': 100}}


print('Вы находитесь в меню редактирования!')
while True:
    choice = input(
        """1. Добавить товар в раздел
2. Удалить товар из раздела
3. Вывести все товары и разделы
4. Вывести товары выбранного раздела
5. Повысить/Снизить цену товаров
6. Удалить раздел
7. Выйти из программы
"""
    )
    match choice:
        case '1':
            entered_group = input('Выберите раздел:\n').lower()
            product = input('Какой продукт добавить?\n').lower()
            if product not in shop[entered_group]:
                cost = int(input('Укажите цену\n'))
                add_products(entered_group, shop, {product: cost})
            else:
                print(f'{product} уже есть в магазине')
        case '2':
            del_products(shop)
        case '3':
            print_all_product(shop)
        case '4':
            choice_group = input('Введите раздел\n').lower()
            if choice_group in shop:
                print_group_product(shop, choice_group)
            else:
                print(f'Такого {choice_group} не существует')
        case '5':
            change_price_product(shop, choice)
        case '6':
            group_del(shop)
        case '7':
            print('Выход из программы!')
            break
        case _:
            print('Ошибка, ввведите число от 1 до 7!')
