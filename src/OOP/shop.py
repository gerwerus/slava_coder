# Напишите небольшой магазинчик, который торгует фильмами и книгами.
# Создайте класс продукта, у экземпляров которого есть два поля: цена, название.
# Унаследуйте от этого класса два других: книги и фильма соответственно. Своих переменных у этих классов пока нет.
# Создайте 5 экземпляров класса книги и 5 экземпляров класса фильма (в интернете найдите названия, а цены придумайте).
# Дальше создайте класс магазина в котором будет лежать данные товары.
# Реализуйте вывод товаров, покупку товара, подсчёт суммы товаров из корзины пользователя.
# https://i.imgur.com/kJ1wEnR.png
COUNT_PRODUCTS_MIN = 1


def main():
    products = [
        Book('Идиот', 250),
        Book('Мастер и Маргарита', 500),
        Book('Человек, который смеется', 750),
        Book('О дивный новый мир', 430),
        Book('Последний день приговоренного к смерти', 370),
        Film('Титаник', 1000),
        Film('Бойцовский клуб', 750),
        Film('F1', 1500),
        Film('Аватар', 1234),
        Film('Титаникус', 4321),
    ]
    shop = Shop(products)
    result_cost = 0
    while True:
        shop.print_products()
        print('0. Выход')

        try:
            product_choice = int(input('Введите номер товара, какой хотите приборести:\n'))
            if product_choice == 0:
                break
            if product_choice < COUNT_PRODUCTS_MIN or product_choice > len(shop.products):
                print('Неверный номер товара.')
                continue

            result_cost = shop.buy_products(product_choice, result_cost)
            print(f'Стоимость товаров из корзины: {result_cost}')

        except ValueError:
            print('Пожалуйста, введите число.')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Book(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = 'Книга'

    def __repr__(self):
        return f'({self.type}. {self.name!r}, {self.price!r})'


class Film(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = 'Фильм'

    def __repr__(self):
        return f'({self.type}. {self.name!r}, {self.price!r})'


class Shop:
    def __init__(self, products):
        self.products = products

    def print_products(self):
        for i, product in enumerate(self.products):
            print(f'{i + 1}. {product.type}: {product.name}. Цена: {product.price}')

    def buy_products(self, product_choice, current_cost):
        products = self.products[product_choice - 1]
        print(f'В корзину добавлен товар {products.type}. {products.name}')
        self.products.pop(product_choice - 1)
        return current_cost + products.price


if __name__ == '__main__':
    main()
