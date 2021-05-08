import time
from itertools import cycle


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self):

        c = 0
        for el in cycle(TrafficLight.__color):
            if c == 6:
                print('Хватить смотреть на светофор! Переходите дорогу!')
                break
            print(el)
            if el == "красный":
                time.sleep(7)
            elif el == "желтый":
                time.sleep(2)
            else:
                time.sleep(5)
            c = c + 1

s = TrafficLight()
s.running()
