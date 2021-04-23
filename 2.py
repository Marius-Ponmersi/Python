# Работает только с нечетным количеством элементов списка
spisok = input("Введите через пробел элементы списка: ").split()
print(spisok)
print(len(spisok))
new = ''

for el in range(len(spisok)):
    el = 0
    while el < (len(spisok) - 1):
        tmp = spisok[el]
        spisok[el] = spisok[el + 1]
        spisok[el + 1] = tmp
        el = el + 2

new = ''.join(spisok)
new_spisok = list(new)
print(new_spisok)
