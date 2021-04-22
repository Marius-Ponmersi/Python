p = ["название", "цена", "количество", "ед"]  # Параметры

name_1 = input("Введите названия товара 1: ")
price_1 = float(input("Введите цену товара 1: "))
amount_1 = int(input("Введите количество товара 1: "))
unit = "шт."
t_1 = [name_1, price_1, amount_1, unit]  # Товар 1
tovar_1 = dict(zip(p, t_1))

name_2 = input("Введите названия товара 2: ")
price_2 = float(input("Введите цену товара 2: "))
amount_2 = int(input("Введите количество товара 2: "))
t_2 = [name_2, price_2, amount_2, unit]  # Товар 2
tovar_2 = dict(zip(p, t_2))

name_3 = input("Введите названия товара 3: ")
price_3 = float(input("Введите цену товара 3: "))
amount_3 = int(input("Введите количество товара 3: "))
t_3 = [name_3, price_3, amount_3, unit]  # Товар 2
tovar_3 = dict(zip(p, t_3))

structura = [(1, tovar_1), (2, tovar_2), (3, tovar_3)]
print(f'Структура: {structura}')

analitika = {p[0]:(name_1, name_2, name_3), p[1]: (price_1, price_2, price_3), p[2]: (amount_1, amount_2, amount_3), p[3]: unit}
print(f'Аналитика: {analitika}')

