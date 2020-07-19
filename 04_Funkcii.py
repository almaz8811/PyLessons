'''
Функции
'''
percent_sale = abs(int(input('Введите размер скидки: ')))
price_goods = {
    'iphone6': 50000,
    'iphone7': 70000,
    'iphone8': -80000
}

def price_sale(price, percent, max_percent = 30):
    price = abs(price)  # С помощью abs() убираем знак минус у цены товара
    if percent > max_percent:
        total = price - price * max_percent / 100
        print(f'Цена {key} с максимальной скидкой {max_percent}% - {total} руб.')
    else:
        total = price - price * percent / 100
        print(f'Цена {key} со скидкой {percent}% - {total} руб.')
    return int(total)

""" for key in price_goods:
    price_sale(price_goods[key], percent_sale) """

for key in price_goods:
    price_goods[key] = price_sale(price_goods[key], percent_sale, max_percent = 100)
    # price_goods[key] = price_sale(price_goods[key], percent_sale, 100)

print(f'\nЦены с учетом скидки - {price_goods}')