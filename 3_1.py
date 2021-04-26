def my_func(arg_1, arg_2):
    if arg_2 == 0:
        print("На ноль делить нельзя!")
        return
    return arg_1 / arg_2
print(my_func(float(input(f'Введите число: ')), float(input(f'Введите число: '))))
