class OwnError(Exception):
    def __init__(self, text):
        self.text = text


def check_number():
    spisok = []
    while True:
        li = input('Введите числа через пробел, для выхода - stop: ').split()
        for el in li:
            if el == 'stop':
                return spisok
            else:
                try:
                    spisok.append(int(el))
                    # if el not in '0123456789':
                    #     raise OwnError('Вы ввели не число. Для выхода - stop')

                except ValueError:
                    print('Вы ввели не число. Для выхода - stop')
                except OwnError as err:
                    print(err)
        print(spisok)


print(check_number())
