import math
class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus - other.nucleus > 0:
            return Cell(self.nucleus - other.nucleus)
        else:
            return 'Нельзя выполнить разность, т.к. вторая клетка больше первой'

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus / other.nucleus)

    def __str__(self):
        return f'Клетка с числом ячеек: {math.trunc(self.nucleus)}'

    def make_order(self):
        stroka = self.nucleus * '*'
        print("\n".join([stroka[j:j + 5] for j in range(0, len(stroka), 5)]))


c1 = Cell(14)
c2 = Cell(5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
c1.make_order()