class ComplexNumbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return ComplexNumbers(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumbers(self.number * other.number)

    def __str__(self):
        return f'Результат равен: {self.number}'


cn1 = ComplexNumbers(1 + 1j)
cn2 = ComplexNumbers(2 + 4j)
print(cn1 + cn2)
print(cn1 * cn2)
