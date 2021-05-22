a = input("Введите число: ")
b = input("Введите число: ")

class OwnError(Exception):
    def __init__(self, text):
        self.text = text
try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise OwnError('На ноль делить нельзя!')
    else:
        res = a / b
except ValueError:
    print('Вы ввели не число!')
except OwnError as err:
    print(err)
else:
    print(f'Деление произошло. Результат: {res}')
finally:
    print("Работа программы завершена")
