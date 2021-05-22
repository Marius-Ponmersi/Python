class Storehouse:
    def __init__(self):
        pass

class Office_equipment:
    def __init__(self, type, count):
        self.type = type
        self.model = model
        self.count = count
        print(f'Тип: {type}, количество: {count}')


class Printer(Office_equipment):
    def __init__(self, name, model, count):
        self.name = name
        self.model = model
        self.count = count
        print(f'Фирма-производитель: {name}, модель:  {model}, количество: {count}')

class Scanner(Office_equipment):
    def __init__(self, name, model, count):
        self.name = name
        self.model = model
        self.count = count
        print(f'Фирма-производитель: {name}, модель:  {model}, количество: {count}')

class Xerox(Office_equipment):
    def __init__(self, name, model, count):
        self.name = name
        self.model = model
        self.count = count
        print(f'Фирма-производитель: {name}, модель:  {model}, количество: {count}')
