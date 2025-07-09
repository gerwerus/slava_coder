# Написать программу магазина с функциями:
# 3.1) Для администратора:
# а) Добавление товара в магазин
# б) Удаление товара из магазина
# в) Изменение цены товара в магазине
# г) Процентная наценка на все товара в магазине
# д) Добавление раздела в магазин
# 3.2) Для обычного пользователя:
# а) Покупка товара и добавление его в корзину
# б) Функция добавления замечаний и предложений
# 3.3) Общие:
# а) Вывод списка всех товаров с ценами
# б) Вывод списка всех товаров выбранного раздела


# добавление продукта в раздел
def add_product(shop: dict[str, dict[str, int]]) -> None:
    choice_group = input('Выберите в какой раздел добавить товар:\n')
    if choice_group not in shop:
        print('Такого раздела не существует')
        return

    choice_product = input('Какой продукт добавить в раздел?\n')
    if choice_product in shop[choice_group]:
        print('Такой продукт уже существует!')
        return

    choice_price_product = int(input('Установите цену товара:\n'))
    shop[choice_group].update({choice_product: choice_price_product})
    print(f'Добавлен товар {choice_product} с ценой {choice_price_product} рублей')


# удаление продукта из раздела
def del_product(shop: dict[str, dict[str, int]]) -> None:
    choice_group = input('Выберите из какого раздела удалить товар:\n')
    if choice_group not in shop:
        print('Такого раздела не существует')
        return

    choice_product = input('Какой продукт удалить из раздела?\n')
    if choice_product not in shop[choice_group]:
        print('Такого продукта нет в магазине')
        return

    del shop[choice_group][choice_product]
    print(f'Товар {choice_product} удален')


# изменение цены продукта
def change_price_product(shop: dict[str, dict[str, int]]) -> None:
    choice_group = input('Выберите раздел:\n')
    if choice_group not in shop:
        print('Такого раздела не существует')
        return

    choice_product = input('Выберите товар для изменения\n')
    if choice_product not in shop[choice_group]:
        print('Такого товара не существует')
        return

    choice_amount = int(input('Введите сумму изменения\n'))
    choice_change = input("""1. Повысить цену
2. Понизить цену
""")
    if choice_change == '1':
        price_new = shop[choice_group][choice_product] + choice_amount

    elif choice_change == '2':
        price_new = shop[choice_group][choice_product] - choice_amount

    else:
        print('Неверно выбрано действие')
        return

    shop[choice_group].update({choice_product: price_new})


# процентная наценка на все товары
def percentage_markup_all_products(shop: dict[str, dict[str, int]]) -> None:
    percentage_markup = int(input('Введите процент наценки:\n'))
    for value in shop.values():
        for product, price in value.items():
            new_price = (price * percentage_markup) / 100 + price
            value.update({product: new_price})


# добавление раздела
def add_group(shop: dict[str, dict[str, int]]) -> None:
    entered_group = input('Введите раздел, который хотите добавить:\n')
    if entered_group in shop:
        print('Такой раздел уже существует')
        return

    shop.update({entered_group: {}})
    print(f'Раздел {entered_group} добавлен в магазин')


# покупка и добавление товара в корзину
def buy_add_to_cart(shop: dict[str, dict[str, int]], shop_cart: list) -> None:
    choice_group = input('Выберите раздел\n')
    if choice_group not in shop:
        print('Такого раздела не существует')
        return

    choice_product = input('Какой продукт хотите купить?\n')
    if choice_product not in shop[choice_group]:
        print('Такого продукта не существует')
        return

    shop_cart.append(choice_product)
    print(shop_cart)


# функция оставления отзыва
def add_reviews(reviews: dict) -> None:
    review_text = input('Оставьте ваши замечания или пожелания:\n')
    reviews.update({username: review_text})


# печать всех продуктов
def print_all_product(shop: dict[str, dict[str, int]]) -> None:
    for group, array in shop.items():
        print(f'Раздел: {group}')
        for products, price in array.items():
            print(products + ' - ' + str(price))


# печать выбранного раздела
def print_group_product(shop: dict[str, dict[str, int]]) -> None:
    choice_group = input('Выберите раздел\n')
    for product, price in shop[choice_group].items():
        print(f'{product} - {price}')


ADMIN_ACTIONS = {
    '1': add_product,
    '2': del_product,
    '3': change_price_product,
    '4': percentage_markup_all_products,
    '5': add_group,
    '6': print_all_product,
    '7': print_group_product,
}
USER_ACTIONS = {
    '1': buy_add_to_cart,
    '2': add_reviews,
    '3': print_all_product,
    '4': print_group_product,
}
shop = {'мучное': {'хлеб': 50, 'пряники': 70}, 'молочное': {'молоко': 100, 'кефир': 75}}
print('Welcome to MAGAZINE!')
username = input('Введите ваше имя:\n')
while True:
    # панель администратора
    if username == 'admin':
        print('Система редактирования:')
        choice = input("""1. Добавление товара в магазин
2. Удаление товара из магазина
3. Изменение цены товара в магазине
4. Процентная наценка на все товары в магазине
5. Добавление раздела в магазин
6. Вывод списка всех товаров с ценами
7. Вывод списка всех товаров выбранного раздела
""")
        if choice in ADMIN_ACTIONS:
            ADMIN_ACTIONS[choice](shop)
        else:
            print('Неверно выбрано действие')

    # панель покупателя
    else:
        print(f'Добро пожаловать {username}!')
        choice = input("""1. Купить товар
2. Оставить замечание или предложение
3. Вывод списка всех товаров с ценами
4. Вывод списка всех товаров выбранного раздела
""")
        if choice in USER_ACTIONS:
            action = USER_ACTIONS[choice]
            if choice == '1':
                shop_cart = []
                action(shop, shop_cart)
            elif choice == '2':
                reviews = {}
                action(reviews)
            else:
                action(shop)
        else:
            print('Неверно выбрано действие')
