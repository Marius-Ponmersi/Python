
n = 1 # Начальный номер дня
a = float(input("Введите сколько км пробежал спортсмен в первый день: "))
b = float(input("Введите сколько км должен пробежать спортсмен: "))
while a < b:
    print(f"{n}-ый день: {a}")
    a = a + a/10
    n += 1
print(f"{n}-ый день: {a}")
print(f"На {n}-ый день спортсмен достиг результата - не менее {b}")

'''

# Вариант с использованием break (но не показывает 1-ый день)
n = 1 # Начальный номер дня
a = float(input("Введите сколько км пробежал спортсмен в первый день: "))
b = float(input("Введите сколько км должен пробежать спортсмен: "))
while True:
    a *= 1.1
    n += 1
    if a >= b:
        print(f"{n}-ый день: {a}")
        print(f"На {n}-ый день спортсмен достиг результата - не менее {b}")
        break
    print(f"{n}-ый день: {a}")

'''
