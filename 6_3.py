class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'CEO'
    dict = {'wage': 1000000, 'bonus': 500000}
    __income = dict['wage'] + dict['bonus']

w = Worker()

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {Position.name} {Position.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {p._Worker__income}')

p = Position()
p.get_full_name()
p.get_total_income()
