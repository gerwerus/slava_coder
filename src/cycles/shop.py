def product_delete_func():
    for i in shop:
        if str(i[0]) == product_delete:
            shop.remove(i)
def product_add_func():
    if str(shop[0]) != product_add:
        product_m = [product_add, product_cost]
        shop.append(product_m)
def shop_found_func():
    for product_array in shop:
        print(product_array[0], '-', product_array[1], ' р.')
money = 500
bag = []

shop = [['котлеты', 100], ['гречка', 234], ['хлеб', 54]]

print('Добро пожаловать в наш магазин!')
username = input('Введите ваше имя: ')

if username.lower() == 'admin': # КОД ДЛЯ АДМИНИСТРАТОРА
    print(f'В магазине сейчас имеются товары такие как: {shop}')
    while True:
        choice_adm = input('Выберите, удалить/добавить товар или выйти из системы: ').lower()
        if choice_adm == 'удалить':
            product_delete = input('Введите название товара, который хотите удалить: ').lower()
            product_delete_func() # УДАЛЕНИЕ ТОВАРА
            print(f'Товар {product_delete} удален')
        elif choice_adm == 'добавить':
            product_add = input('Введите название товара, который хотите добавить: ').lower()
            product_cost = int(input('Введите цену товара: '))
            product_add_func() # ДОБАВЛЕНИЕ ТОВАРА
            print(f'Товар {product_add} добавлен')
        elif choice_adm == 'выйти':
            print('Вы вышли из системы!')
            break
        print('Обновленный список товаров: ', shop)
elif username.lower() != 'admin': # КОД ДЛЯ ПОКУПАТЕЛЯ
    while True:
        choice = input('Будете что-то приобретать? ')
        if choice.lower() == 'да':
            print('В магазине имеются товар: ')
            shop_found_func() # ПОИСК ТОВАРА
            print('Сейчас у вас ', money, ' рублей')
            print('В сумке сейчас находятся: ')
            for i in bag: # ПРОВЕРКА ДЕНЕГ
                print(i)
            if money <= 54:
                print('У вас недостаточно средств для покупок!')
                break
            product_choice = input('Что будете преобретать? ')
            found = False
            for product_array in shop: # ПОКУПКА ТОВАРА
                if product_choice == product_array[0] and money >= product_array[1]:
                    money -= product_array[1]
                    bag.append(product_array[0])
                    print('С счёта списано ', product_array[1], ' рублей и ', product_array[0], ' добавлено в сумку')
                    found = True
            if not found:
                 print('Такой товар не найден:')
        elif choice.lower() =='нет':
            print('Выход из магазина')
            break
