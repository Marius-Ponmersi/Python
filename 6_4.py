delimeter = '*' * 50
print(delimeter)

class Car:
    speed = 120
    color = 'white'
    name = 'toyota'
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {Car.speed}')

c = Car()
print(f'Car: {c.speed}, {c.color}, {c.name}, {c.is_police}')
c.go()
c.stop()
c.turn('налево')
c.show_speed()
print(delimeter)

class TownCar(Car):
    speed = 80
    name = 'reno'
    is_police = False

    def show_speed(self):
        if TownCar.speed > 60:
            print('Превышение скорости!!!')
        else:
            print(Car.speed)

t = TownCar()
print(f'TownCar: {t.speed}, {t.color}, {t.name}, {t.is_police}')
t.go()
t.stop()
t.turn('направо')
t.show_speed()
print(delimeter)

class SportCar(Car):
    speed = 200
    color = 'red'
    name = 'ferrari'
    is_police = False

s = SportCar()
print(f'SportCar: {s.speed}, {s.color}, {s.name}, {s.is_police}')
s.go()
s.stop()
s.turn('направо')
s.show_speed()
print(delimeter)

class WorkCar(Car):
    speed = 50
    color = 'black'
    name = 'ЗИЛ'
    is_police = False

    def show_speed(self):
        if WorkCar.speed > 40:
            print('Превышение скорости!!!')
        else:
            print(WorkCar.speed)

w = WorkCar()
print(f'WorkCar: {w.speed}, {w.color}, {w.name}, {w.is_police}')
w.go()
w.stop()
w.turn('назад')
w.show_speed()
print(delimeter)

class PoliceCar(Car):
    color = 'blue'
    name = 'dodge'
    is_police = True

p = PoliceCar()
print(f'PoliceCar: {p.speed}, {p.color}, {p.name}, {p.is_police}')
p.go()
p.stop()
p.turn('в участок')
p.show_speed()
print(delimeter)
