'''
def my_func(x,y):
    return x ** y
print(my_func(abs(float(input("Введите x - действительное  число: "))), abs(int(input("Введите y - целое число: "))) * (-1)))
'''

n = 1
x = abs(float(input("Введите x - действительное  число: ")))
y = abs(int(input("Введите y - целое число: ")))
a = x
while n <= y:
    x = a * x
    n = n + 1
    if n == y:
        print(1 / x)


