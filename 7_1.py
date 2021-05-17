class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        spisok = []
        for row in self.data:
            spisok.append(' '.join(map(str, row)))
        stroka = '\n'.join(spisok)
        return stroka

    def __add__(self, other):
        data = []

        for j in range(len(self.data)):
            data.append([])
            for k in range(len(self.data[0])):
                data[j].append(self.data[j][k] + other.data[j][k])

        return Matrix(data)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(m1)
print('**********')
print(m2)
print('**********')
print(m1 + m2)