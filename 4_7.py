from math import factorial

'''
n = int(input('Введите число: '))
spisok = [el for el in range(1, n + 1)]
print(spisok)


def fac():
    for el in spisok:
        yield factorial(el)


print(fac())
for el in fac():
    print(el)

'''

n = int(input('Введите число n: '))


def fact(n):
    for el in range(1, n + 1):
        yield factorial(el)


print(fact(n))
for el in fact(n):
    print(el)
