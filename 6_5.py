class Stationery:
    title = 'pen'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Чернила')

class Pencil(Stationery):
    def draw(self):
        print('Грифель')

class Handle(Stationery):
    def draw(self):
        print('Спирт')

r = Pen()
r.draw()

k = Pencil()
k.draw()

m = Handle()
m.draw()
