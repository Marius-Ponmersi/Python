time = int(input("Введите время в секундах: "))
h = time // 3600
m = time % 3600 // 60
s = time % 3600 % 60
print(f"{h}:{m}:{s}")