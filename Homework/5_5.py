numbers_stroka = input('Введите числа через пробел: ')

f_write = open('5_5.txt', 'w')
numbers_string = f_write.write(numbers_stroka)
f_write.close()

f_read = open('5_5.txt', 'r')
l = [line.strip() for line in f_read]
for el in l:
    numbers = [float(number) for number in el.split()]
print(sum(numbers))
f_read.close()
