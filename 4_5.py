from functools import reduce
spisok = [el for el in range(100, 1001, 2)]
print(spisok)
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, spisok))