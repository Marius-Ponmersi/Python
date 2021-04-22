spisok = input("Введите через пробел элементы списка: ").split()
print(spisok)
a = 0
n = len(spisok)

for el in spisok:
    if a < n:
        spisok.insert(a + 1, el[a])
    a += 2
print(spisok)

