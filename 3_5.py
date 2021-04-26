a = input("Введите числа через пробел: ").split()
b = [int(el) for el in a]

for el in b:
    summa = sum(b)
    print(summa)
    while True:
        a = input("Введите числа через пробел: ").split()
        b = [int(el) for el in a]
        summa = summa + sum(b)
        print(summa)
    if input("Введите числа через пробел: ").isdigit() == False:
            break

