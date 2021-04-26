def my_func(arg_1, arg_2, arg_3):
    list = [arg_1, arg_2, arg_3]
    list.sort()
    return list[1] + list[2]

print(my_func(float(input("Введите число: ")), float(input("Введите число: ")), float(input("Введите число: "))))
